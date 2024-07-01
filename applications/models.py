from django.db import models


class I90Application(models.Model):
    # Part 1. Information About You
    a_number = models.CharField(max_length=250, blank=True, null=True)
    usci_number = models.CharField(max_length=250, blank=True, null=True)

    # Your Full Name
    family_name = models.CharField(max_length=250, blank=True, null=True)
    given_name = models.CharField(max_length=250, blank=True, null=True)
    middle_name = models.CharField(max_length=250, blank=True, null=True)
    name_change_yes = models.BooleanField(default=False, blank=True, null=True)
    name_change_no = models.BooleanField(default=False, blank=True, null=True)
    name_change_na = models.BooleanField(default=False, blank=True, null=True)
    name_change_family_name = models.CharField(
        max_length=250, blank=True, null=True)
    name_change_first_name = models.CharField(
        max_length=250, blank=True, null=True)
    name_change_middle_name = models.CharField(
        max_length=250, blank=True, null=True)

    # Mailing Address
    mailing_name = models.CharField(max_length=250, blank=True, null=True)
    street_name_number = models.CharField(
        max_length=250, blank=True, null=True)
    apt = models.BooleanField(default=False, blank=True, null=True)
    ste = models.BooleanField(default=False, blank=True, null=True)
    flr = models.BooleanField(default=False, blank=True, null=True)
    city_town = models.CharField(max_length=250, blank=True, null=True)
    state = models.CharField(max_length=250, blank=True, null=True)
    zip_code = models.CharField(max_length=250, blank=True, null=True)
    province = models.CharField(max_length=250, blank=True, null=True)
    postal_code = models.CharField(max_length=250, blank=True, null=True)
    country = models.CharField(max_length=250, blank=True, null=True)

    # Physical Address
    physical_street_name_number = models.CharField(
        max_length=250, blank=True, null=True)
    physical_apt = models.BooleanField(default=False, blank=True, null=True)
    physical_ste = models.BooleanField(default=False, blank=True, null=True)
    physical_flr = models.BooleanField(default=False, blank=True, null=True)
    physical_city_town = models.CharField(
        max_length=250, blank=True, null=True)
    physical_state = models.CharField(max_length=250, blank=True, null=True)
    physical_zip_code = models.CharField(max_length=250, blank=True, null=True)
    physical_province = models.CharField(max_length=250, blank=True, null=True)
    physical_postal_code = models.CharField(
        max_length=250, blank=True, null=True)
    physical_country = models.CharField(max_length=250, blank=True, null=True)

    # Information About You
    gender_male = models.BooleanField(default=False, blank=True, null=True)
    gender_female = models.BooleanField(default=False, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    birth_city_town = models.CharField(max_length=250, blank=True, null=True)
    birth_country = models.CharField(max_length=250, blank=True, null=True)
    mother_first_name = models.CharField(max_length=250, blank=True, null=True)
    father_first_name = models.CharField(max_length=250, blank=True, null=True)
    class_of_admission = models.CharField(
        max_length=250, blank=True, null=True)
    date_of_admission = models.DateField(blank=True, null=True)
    ssn = models.CharField(max_length=250, blank=True, null=True)

    # Part 2. Application Type
    lawful_permanent_resident = models.BooleanField(
        default=False, blank=True, null=True)
    permanent_resident = models.BooleanField(
        default=False, blank=True, null=True)
    conditional_permanent_resident = models.BooleanField(
        default=False, blank=True, null=True)

    # Reason for Application
    # Section A
    previous_card_lost = models.BooleanField(
        default=False, blank=True, null=True)
    previous_card_never_received = models.BooleanField(
        default=False, blank=True, null=True)
    existing_card_mutilated = models.BooleanField(
        default=False, blank=True, null=True)
    existing_card_incorrect_data_DHS = models.BooleanField(
        default=False, blank=True, null=True)
    biographic_information_legally_changed = models.BooleanField(
        default=False, blank=True, null=True)
    existing_card_expired = models.BooleanField(
        default=False, blank=True, null=True)
    my_14_birthday_registering_after = models.BooleanField(
        default=False, blank=True, null=True)
    my_14_birthday_registering_before = models.BooleanField(
        default=False, blank=True, null=True)
    permanent_resident = models.BooleanField(
        default=False, blank=True, null=True)
    port_of_entry = models.CharField(max_length=250, blank=True, null=True)
    commuter = models.BooleanField(default=False, blank=True, null=True)
    convertered_to_lawful_permanent_resident = models.BooleanField(
        default=False, blank=True, null=True)
    prior_edition_alien_registration_card = models.BooleanField(
        default=False, blank=True, null=True)

    # Section B
    previous_card_lost_B = models.BooleanField(
        default=False, blank=True, null=True)
    previous_card_never_received_B = models.BooleanField(
        default=False, blank=True, null=True)
    existing_card_mutilated_B = models.BooleanField(
        default=False, blank=True, null=True)
    existing_card_incorrect_data_DHS_B = models.BooleanField(
        default=False, blank=True, null=True)
    biographic_information_legally_changed_B = models.BooleanField(
        default=False, blank=True, null=True)

    # Part 3. Processing Information
    immigrant_visa_adjustment_location = models.CharField(
        max_length=250, blank=True, null=True)
    immigrant_visa_issued_location = models.CharField(
        max_length=250, blank=True, null=True)
    us_destination_at_admission = models.CharField(
        max_length=250, blank=True, null=True)
    port_of_entry_2 = models.CharField(max_length=250, blank=True, null=True)
    ever_exclusion_deportation_removal_proceedings_yes = models.BooleanField(
        default=False, blank=True, null=True)
    ever_exclusion_deportation_removal_proceedings_no = models.BooleanField(
        default=False, blank=True, null=True)
    ever_filed_form_abandonment_by_alien_of_status_yes = models.BooleanField(
        default=False, blank=True, null=True)
    ever_filed_form_abandonment_by_alien_of_status_no = models.BooleanField(
        default=False, blank=True, null=True)

    # Biographic Information
    ethnicity_hispanic_latino = models.BooleanField(
        default=False, blank=True, null=True)
    ethnicity_not_hispanic_latino = models.BooleanField(
        default=False, blank=True, null=True)
    ethnicity_white = models.BooleanField(default=False, blank=True, null=True)
    ethnicity_asian = models.BooleanField(default=False, blank=True, null=True)
    ethnicity_black = models.BooleanField(default=False, blank=True, null=True)
    ethnicity_american_indian = models.BooleanField(
        default=False, blank=True, null=True)
    ethnicity_native_hawaiian = models.BooleanField(
        default=False, blank=True, null=True)
    height_feet = models.CharField(max_length=250, blank=True, null=True)
    height_inch = models.CharField(max_length=250, blank=True, null=True)
    weight = models.CharField(max_length=250, blank=True, null=True)
    eye_color_black = models.BooleanField(default=False, blank=True, null=True)
    eye_color_blue = models.BooleanField(default=False, blank=True, null=True)
    eye_color_brown = models.BooleanField(default=False, blank=True, null=True)
    eye_color_gray = models.BooleanField(default=False, blank=True, null=True)
    eye_color_green = models.BooleanField(default=False, blank=True, null=True)
    eye_color_hazel = models.BooleanField(default=False, blank=True, null=True)
    eye_color_maroon = models.BooleanField(
        default=False, blank=True, null=True)
    eye_color_pink = models.BooleanField(default=False, blank=True, null=True)
    eye_color_unknown = models.BooleanField(
        default=False, blank=True, null=True)
    hair_color_bald = models.BooleanField(default=False, blank=True, null=True)
    hair_color_black = models.BooleanField(
        default=False, blank=True, null=True)
    hair_color_blond = models.BooleanField(
        default=False, blank=True, null=True)
    hair_color_brown = models.BooleanField(
        default=False, blank=True, null=True)
    hair_color_gray = models.BooleanField(default=False, blank=True, null=True)
    hair_color_red = models.BooleanField(default=False, blank=True, null=True)
    hair_color_sandy = models.BooleanField(
        default=False, blank=True, null=True)
    hair_color_white = models.BooleanField(
        default=False, blank=True, null=True)
    hair_color_unknown = models.BooleanField(
        default=False, blank=True, null=True)

    # Part 4. Accommodations for Individuals with Disabilities and/or Impairments
    accommodation_because_disabilities = models.BooleanField(
        default=False, blank=True, null=True)
    deaf = models.BooleanField(default=False, blank=True, null=True)
    deaf_more = models.TextField(blank=True, null=True)
    blind = models.BooleanField(default=False, blank=True, null=True)
    blind_more = models.TextField(blank=True, null=True)
    other = models.BooleanField(default=False, blank=True, null=True)
    other_more = models.TextField(blank=True, null=True)

    # Part 5. Applicant's Statement, Contact Information, Certification, and Signature
    applicant_able_understand_english = models.BooleanField(
        default=False, blank=True, null=True)
    applicant_request_interpreter = models.BooleanField(
        default=False, blank=True, null=True)
    interpreter_read_language = models.CharField(
        max_length=250, blank=True, null=True)
    my_request = models.BooleanField(
        default=False, blank=True, null=True)
    my_request_name = models.CharField(
        max_length=250, blank=True, null=True)
    applicant_contact_phone_number = models.CharField(
        max_length=250, blank=True, null=True)
    applicant_contact_mobile_number = models.CharField(
        max_length=250, blank=True, null=True)
    applicant_contact_email = models.EmailField(blank=True, null=True)
    applicant_signature = models.ImageField(
        upload_to='signatures/', blank=True, null=True)
    applicant_signature_date = models.DateField(blank=True, null=True)

    # Part 6. Interpreter's Contact Information, Certification, and Signature
    interpreter_first_name = models.CharField(
        max_length=250, blank=True, null=True)
    interpreter_last_name = models.CharField(
        max_length=250, blank=True, null=True)
    interpreter_business_organization = models.CharField(
        max_length=250, blank=True, null=True)
    interpreter_street_number_name = models.CharField(
        max_length=250, blank=True, null=True)
    interpreter_apt = models.BooleanField(default=False, blank=True, null=True)
    interpreter_ste = models.BooleanField(default=False, blank=True, null=True)
    interpreter_flr = models.BooleanField(default=False, blank=True, null=True)
    interpreter_city_town = models.CharField(
        max_length=250, blank=True, null=True)
    interpreter_state = models.CharField(max_length=250, blank=True, null=True)
    interpreter_zip_code = models.CharField(
        max_length=250, blank=True, null=True)
    interpreter_province = models.CharField(
        max_length=250, blank=True, null=True)
    interpreter_postal_code = models.CharField(
        max_length=250, blank=True, null=True)
    interpreter_country = models.CharField(
        max_length=250, blank=True, null=True)
    interpreter_phone_number = models.CharField(
        max_length=250, blank=True, null=True)
    interpreter_mobile_number = models.CharField(
        max_length=250, blank=True, null=True)
    interpreter_email = models.EmailField(blank=True, null=True)
    other_language = models.CharField(max_length=10, blank=True, null=True)
    interpreter_signature = models.ImageField(
        upload_to='signatures/', blank=True, null=True)
    interpreter_signature_date = models.DateField(blank=True, null=True)

    # Part 7. Contact Information, Declaration, and Signature of the Person Preparing This Application
    preparer_last_name = models.CharField(
        max_length=250, blank=True, null=True)
    preparer_first_name = models.CharField(
        max_length=250, blank=True, null=True)
    preparer_business_organization = models.CharField(
        max_length=250, blank=True, null=True)
    preparer_street_number_name = models.CharField(
        max_length=250, blank=True, null=True)
    preparer_apt = models.BooleanField(default=False, blank=True, null=True)
    preparer_ste = models.BooleanField(default=False, blank=True, null=True)
    preparer_flr = models.BooleanField(default=False, blank=True, null=True)
    preparer_city_town = models.CharField(
        max_length=250, blank=True, null=True)
    preparer_state = models.CharField(max_length=250, blank=True, null=True)
    preparer_zip_code = models.CharField(max_length=250, blank=True, null=True)
    preparer_province = models.CharField(max_length=250, blank=True, null=True)
    preparer_postal_code = models.CharField(
        max_length=250, blank=True, null=True)
    preparer_country = models.CharField(max_length=250, blank=True, null=True)
    preparer_phone_number = models.CharField(
        max_length=250, blank=True, null=True)
    preparer_mobile_number = models.CharField(
        max_length=250, blank=True, null=True)
    preparer_email = models.EmailField(blank=True, null=True)
    not_an_attorney = models.BooleanField(default=False)
    an_attorney = models.BooleanField(default=False)
    an_attorney_extends = models.BooleanField(default=False)
    an_attorney_not_extends = models.BooleanField(default=False)
    preparer_signature = models.ImageField(
        upload_to='signatures/', blank=True, null=True)
    preparer_signature_date = models.DateField(blank=True, null=True)
    pdf_file = models.FileField(
        upload_to='filled_pdfs/', blank=True, null=True)
