import os
from django.http import HttpResponse
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from .models import I90Application
from .serializers import I90ApplicationSerializer
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from .forms import I90ApplicationForm
import fitz


def fill_pdf(form_data, template_path, output_path):
    field_mapping = {
        "a_number": "form1[0].#subform[0].P1_Line1_AlienNumber0",
        "usci_number": "form1[0].#subform[0].P1_Line2_AcctIdentifier[0]",
        "family_name": "form1[0].#subform[0].P1_Line3a_FamilyName[0]",
        "given_name": "form1[0].#subform[0].P1_Line3b_GivenName[0]",
        "middle_name": "form1[0].#subform[0].P1_Line3c_MiddleName[0]",
        "name_change_yes": "form1[0].#subform[0].P1_checkbox4[0]",
        "name_change_no": "form1[0].#subform[0].P1_checkbox4[1]",
        "name_change_na": "form1[0].#subform[0].P1_checkbox4[2]",
        "name_change_family_name": "form1[0].#subform[0].P1_Line5a_FamilyName[0]",
        "name_change_first_name": "form1[0].#subform[0].P1_Line5b_GivenName[0]",
        "name_change_middle_name": "form1[0].#subform[0].P1_Line5c_MiddleName[0]",
        "mailing_name": "form1[0].#subform[0].P1_Line6a_InCareofName[0]",
        "street_name_number": "form1[0].#subform[0].P1_Line6b_StreetNumberName[0]",
        "apt": "form1[0].#subform[0].P1_checkbox6c_Unit[0]",
        "ste": "form1[0].#subform[0].P1_checkbox6c_Unit[1]",
        "flr": "form1[0].#subform[0].P1_checkbox6c_Unit[2]",
        "city_town": "form1[0].#subform[0].P1_Line6d_CityOrTown[0]",
        "state": "form1[0].#subform[0].P1_Line6e_State[0]",
        "zip_code": "form1[0].#subform[0].P1_Line6f_ZipCode[0]",
        "province": "form1[0].#subform[0].P1_Line6g_Province[0]",
        "postal_code": "form1[0].#subform[0].P1_Line6h_PostalCode[0]",
        "country": "form1[0].#subform[0].P1_Line6i_Country[0]",
        "physical_street_name_number": "form1[0].#subform[0].P1_Line7a_StreetNumberName[0]",
        "physical_apt": "form1[0].#subform[0].P1_checkbox7b_Unit[0]",
        "physical_ste": "form1[0].#subform[0].P1_checkbox7b_Unit[1]",
        "physical_flr": "form1[0].#subform[0].P1_checkbox7b_Unit[2]",
        "physical_city_town": "form1[0].#subform[0].P1_Line7c_CityOrTown[0]",
        "physical_state": "form1[0].#subform[0].P1_Line7d_State[0]",
        "physical_zip_code": "form1[0].#subform[0].P1_Line7e_ZipCode[0]",
        "physical_province": "form1[0].#subform[0].P1_Line7f_Province[0]",
        "physical_postal_code": "form1[0].#subform[0].P1_Line7g_PostalCode[0]",
        "physical_country": "form1[0].#subform[0].P1_Line7h_Country[0]",
        "gender_male": "form1[0].#subform[0].P1_Line8_male[0]",
        "gender_female": "form1[0].#subform[0].P1_Line8_female[0]",
        "dob": "form1[0].#subform[1].P1_Line9_DateOfBirth[0]",
        "birth_city_town": "form1[0].#subform[1].P1_Line10_CityTownOfBirth[0]",
        "birth_country": "form1[0].#subform[1].P1_Line11_CountryofBirth[0]",
        "mother_first_name": "form1[0].#subform[1].P1_Line12_MotherGivenName[0]",
        "father_first_name": "form1[0].#subform[1].P1_Line13_FatherGivenName[0]",
        "class_of_admission": "form1[0].#subform[1].P1_Line14_ClassOfAdmission[0]",
        "date_of_admission": "form1[0].#subform[1].P1_Line15_DateOfAdmission[0]",
        "ssn": "form1[0].#subform[1].P1_Line16_SSN[0]",
        "lawful_permanent_resident": "form1[0].#subform[1].P2_checkbox1[0]",
        "permanent_resident": "form1[0].#subform[1].P2_checkbox1[1]",
        "conditional_permanent_resident": "form1[0].#subform[1].P2_checkbox1[2]",
        "previous_card_lost": "form1[0].#subform[1].P2_checkbox2[5]",
        "previous_card_never_received": "form1[0].#subform[1].P2_checkbox2[6]",
        "existing_card_mutilated": "form1[0].#subform[1].P2_checkbox2[7]",
        "existing_card_incorrect_data_DHS": "form1[0].#subform[1].P2_checkbox2[4]",
        "biographic_information_legally_changed": "form1[0].#subform[1].P2_checkbox2[0]",
        "existing_card_expired": "form1[0].#subform[1].P2_checkbox2[1]",
        "my_14_birthday_registering_after": "form1[0].#subform[1].P2_checkbox2[2]",
        "my_14_birthday_registering_before": "form1[0].#subform[1].P2_checkbox2[3]",
        "permanent_resident_2": "form1[0].#subform[1].P2_checkbox2[11]",
        "port_of_entry": "form1[0].#subform[1].P2_Line2h1_CityandState[0]",
        "commuter": "form1[0].#subform[1].P2_checkbox2[9]",
        "convertered_to_lawful_permanent_resident": "form1[0].#subform[1].P2_checkbox2[10]",
        "prior_edition_alien_registration_card": "form1[0].#subform[1].P2_checkbox2[8]",
        "previous_card_lost_B": "form1[0].#subform[1].P2_checkbox3[4]",
        "previous_card_never_received_B": "form1[0].#subform[1].P2_checkbox3[0]",
        "existing_card_mutilated_B": "form1[0].#subform[1].P2_checkbox3[1]",
        "existing_card_incorrect_data_DHS_B": "form1[0].#subform[1].P2_checkbox3[2]",
        "biographic_information_legally_changed_B": "form1[0].#subform[1].P2_checkbox3[3]",
        "immigrant_visa_adjustment_location": "form1[0].#subform[2].P3_Line1_LocationAppliedVisa[0]",
        "immigrant_visa_issued_location": "form1[0].#subform[2].P3_Line2_LocationIssuedVisa[0]",
        "us_destination_at_admission": "form1[0].#subform[2].P3_Line3a_Destination[0]",
        "port_of_entry_2": "form1[0].#subform[2].P3_Line3a1_CityandState[0]",
        "ever_exclusion_deportation_removal_proceedings_yes": "form1[0].#subform[2].P3_checkbox4[1]",
        "ever_exclusion_deportation_removal_proceedings_no": "form1[0].#subform[2].P3_checkbox4[0]",
        "ever_filed_form_abandonment_by_alien_of_status_yes": "form1[0].#subform[2].P3_checkbox5[1]",
        "ever_filed_form_abandonment_by_alien_of_status_no": "form1[0].#subform[2].P3_checkbox5[0]",
        "ethnicity_hispanic_latino": "form1[0].#subform[2].P3_checkbox6[1]",
        "ethnicity_not_hispanic_latino": "form1[0].#subform[2].P3_checkbox6[0]",
        "ethnicity_white": "form1[0].#subform[2].P3_checkbox7_White[0]",
        "ethnicity_asian": "form1[0].#subform[2].P3_checkbox7_Asian[0]",
        "ethnicity_black": "form1[0].#subform[2].P3_checkbox7_Black[0]",
        "ethnicity_american_indian": "form1[0].#subform[2].P3_checkbox7_Indian[0]",
        "ethnicity_native_hawaiian": "form1[0].#subform[2].P3_checkbox7_Hawaiian[0]",
        "height_feet": "form1[0].#subform[2].P3_Line8_HeightFeet[0]",
        "height_inch": "form1[0].#subform[2].P3_Line8_HeightInches[0]",
        "weight": "form1[0].#subform[2].P3_Line9_HeightInches1[0]",
        "eye_color_black": "form1[0].#subform[2].P3_checkbox10[6]",
        "eye_color_blue": "form1[0].#subform[2].P3_checkbox10[0]",
        "eye_color_brown": "form1[0].#subform[2].P3_checkbox10[5]",
        "eye_color_gray": "form1[0].#subform[2].P3_checkbox10[8]",
        "eye_color_green": "form1[0].#subform[2].P3_checkbox10[1]",
        "eye_color_hazel": "form1[0].#subform[2].P3_checkbox10[2]",
        "eye_color_maroon": "form1[0].#subform[2].P3_checkbox10[4]",
        "eye_color_pink": "form1[0].#subform[2].P3_checkbox10[3]",
        "eye_color_unknown": "form1[0].#subform[2].P3_checkbox10[7]",
        "hair_color_bald": "form1[0].#subform[2].P3_checkbox11[0]",
        "hair_color_black": "form1[0].#subform[2].P3_checkbox11[8]",
        "hair_color_blond": "form1[0].#subform[2].P3_checkbox11[1]",
        "hair_color_brown": "form1[0].#subform[2].P3_checkbox11[7]",
        "hair_color_gray": "form1[0].#subform[2].P3_checkbox11[2]",
        "hair_color_red": "form1[0].#subform[2].P3_checkbox11[6]",
        "hair_color_sandy": "form1[0].#subform[2].P3_checkbox11[3]",
        "hair_color_white": "form1[0].#subform[2].P3_checkbox11[5]",
        "hair_color_unknown": "form1[0].#subform[2].P3_checkbox11[4]",
        "accommodation_because_disabilities": "form1[0].#subform[2].P4_checkbox1[0]",
        "deaf": "form1[0].#subform[2].P4_checkbox1a[0]",
        "deaf_more": "form1[0].#subform[2].P4_Line1a_AccomodationRequested[0]",
        "blind": "form1[0].#subform[3].P4_checkbox1b[0]",
        "blind_more": "form1[0].#subform[3].P4_Line1b_AccomodationRequested[0]",
        "other": "form1[0].#subform[3].P4_checkbox1c[0]",
        "other_more": "form1[0].#subform[3].P4_Line1c_AccomodationRequested[0]",
        "applicant_able_understand_english": "form1[0].#subform[3].P5_Checkbox1a[0]",
        "applicant_request_interpreter": "form1[0].#subform[3].P5_Checkbox1b[0]",
        "interpreter_read_language": "form1[0].#subform[3].P5_Line1b_Language[0]",
        "my_request": "form1[0].#subform[3].P5_Checkbox2[0]",
        "my_request_name": "form1[0].#subform[3].P5_Line2_NameofRepresentative[0]",
        "applicant_contact_phone_number": "form1[0].#subform[3].P5_Line3_DaytimePhoneNumber[0]",
        "applicant_contact_mobile_number": "form1[0].#subform[3].P5_Line4_MobilePhoneNumber[0]",
        "applicant_contact_email": "form1[0].#subform[3].P5_Line5_EmailAddress[0]",
        "applicant_signature": "form1[0].#subform[3].P5_Line6a_SignatureofApplicant[0]",
        "applicant_signature_date": "form1[0].#subform[3].P5_Line6b_DateofSignature[0]",

        "interpreter_first_name": "form1[0].#subform[4].P6_Line1b_InterpretersGivenName[0]",
        "interpreter_last_name": "form1[0].#subform[4].P6_Line1a_InterpretersFamilyName[0]",
        "interpreter_business_organization": "form1[0].#subform[4].P6_Line2_NameofBusinessor[0]",
        "interpreter_street_number_name": "form1[0].#subform[4].P6_Line3a_StreetNumberName[0]",
        "interpreter_apt": "form1[0].#subform[4].P6_checkbox3b_Unit[0]",
        "interpreter_ste": "form1[0].#subform[4].P6_checkbox3b_Unit[1]",
        "interpreter_flr": "form1[0].#subform[4].P6_checkbox3b_Unit[2]",
        "interpreter_city_town": "form1[0].#subform[4].P6_Line3c_CityTown[0]",
        "interpreter_state": "form1[0].#subform[4].P6_Line3d_State[0]",
        "interpreter_zip_code": "form1[0].#subform[4].P6_Line3e_ZipCode[0]",
        "interpreter_province": "form1[0].#subform[4].P6_Line3f_Province[0]",
        "interpreter_postal_code": "form1[0].#subform[4].P6_Line3g_PostalCode[0]",
        "interpreter_country": "form1[0].#subform[0].P6_Line3h_Country[0]",
        "interpreter_phone_number": "form1[0].#subform[4].P6_Line4_InterpretersDaytimePhoneNumber[0]",
        "interpreter_mobile_number": "form1[0].#subform[4].P6_Line4_InterpretersDaytimePhoneNumber[1]",
        "interpreter_email": "form1[0].#subform[4].P6_Line5_InterpretersEmailAddress[0]",
        "other_language": "form1[0].#subform[4].P6_Language[0]",
        "interpreter_signature": "form1[0].#subform[4].P6_Line6a_Signature[0]",
        "interpreter_signature_date": "form1[0].#subform[4].P6_Line6b_DateofSignature[0]",

        "preparer_last_name": "form1[0].#subform[4].P7_Line1a_FamilyName[0]",
        "preparer_first_name": "form1[0].#subform[4].P7_Line1b_PreparersGivenName[0]",
        "preparer_business_organization": "form1[0].#subform[4].P7_Line2_NameofBusinessor[0]",
        "preparer_street_number_name": "form1[0].#subform[4].P7_Line3a_StreetNumberName[0]",
        "preparer_apt": "form1[0].#subform[4].P7_checkbox3b_Unit[0]",
        "preparer_ste": "form1[0].#subform[4].P7_checkbox3b_Unit[1]",
        "preparer_flr": "form1[0].#subform[4].P7_checkbox3b_Unit[2]",
        "preparer_city_town": "form1[0].#subform[4].P7_Line3c_CityTown[0]",
        "preparer_state": "form1[0].#subform[4].P7_Line3d_State[0]",
        "preparer_zip_code": "form1[0].#subform[4].P7_Line3e_ZipCode[0]",
        "preparer_province": "form1[0].#subform[4].P7_Line3f_Province[0]",
        "preparer_postal_code": "form1[0].#subform[4].P7_Line3g_PostalCode[0]",
        "preparer_country": "form1[0].#subform[4].P7_Line3h_Country[0]",
        "preparer_phone_number": "form1[0].#subform[4].P7_Line4_PreparersDaytimePhoneNumber[0]",
        "preparer_mobile_number": "form1[0].#subform[4].P7_Line5_PreparersFaxNumber[0]",
        "preparer_email": "form1[0].#subform[4].P7_Line6_PreparersEmailAddress[0]",
        "not_an_attorney": "form1[0].#subform[5].P7_checkbox7[0]",
        "an_attorney": "form1[0].#subform[5].P7_checkbox7[1]",
        "an_attorney_extends": "form1[0].#subform[5].P7_checkbox7Extend[0]",
        "an_attorney_not_extends": "form1[0].#subform[5].P7_checkbox7Extend[1]",
        "preparer_signature": "form1[0].#subform[5].P7_Line8a_SignatureofPreparer[0]",
        "preparer_signature_date": "form1[0].#subform[5].P7_Line8b_DateofSignature[0]"
    }
    try:
        pdf_document = fitz.open(template_path)

        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            annotations = page.annots()

            for annotation in annotations:
                try:
                    if annotation.type[1] == "Widget" and annotation.field_name in field_mapping.values():
                        for key, pdf_field in field_mapping.items():
                            if pdf_field == annotation.field_name and key in form_data:
                                annotation.set_field_text(str(form_data[key]))
                                print(
                                    f"Filling field: {pdf_field} with value: {form_data[key]}")
                                # Example: setting text color to black
                                # Depending on the annotation type, you may use different properties
                                if isinstance(annotation, fitz.TextWidget):
                                    annotation.update(
                                        fontsize=10, text_color=(0, 0, 0))
                                    print(
                                        f"Setting text color for {pdf_field} to black")
                except Exception as e:
                    print(f"Error processing annotation: {e}")

        pdf_document.save(output_path)
        pdf_document.close()
        print(f"PDF saved to {output_path}")

    except Exception as e:
        print(f"Error filling PDF: {e}")


def print_pdf_fields(template_path):
    pdf_document = fitz.open(template_path)
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        widget = page.first_widget
        while widget:
            print(f"Field name: {widget.field_name}")
            widget = widget.next


class I90ApplicationCreateView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=I90ApplicationSerializer)
    def post(self, request):

        serializer = I90ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serialized_data = serializer.data
            print(f"Serialized data: {serialized_data}")
            i90application = serializer.save()
            template_path = os.path.join(
                settings.BASE_DIR, 'templates/pdfs/i-90.pdf')
            output_filename = f'filled_form_{i90application.id}.pdf'
            output_path = os.path.join(
                settings.MEDIA_ROOT, 'filled_pdfs', output_filename)
            # print_pdf_fields(template_path)

            fill_pdf(serialized_data, template_path, output_path)

            i90application.pdf_file.name = os.path.join(
                'filled_pdfs', output_filename)
            i90application.save()

            with open(output_path, 'rb') as f:
                response = HttpResponse(
                    f.read(), content_type='application/pdf')
                response['Content-Disposition'] = f'inline; filename="{output_filename}"'
                return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
