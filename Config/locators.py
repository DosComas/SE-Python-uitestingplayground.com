class Locators:
    """Stores the locators of the web elements to be used"""

    # Sample App
    sample_app_link = '//a[contains(@href,"/sampleapp")]'
    sample_app_user = '//input[@type="text"]'
    sample_app_pass = '//input[@type="password"]'
    sample_app_login = '//button[@id="login"]'
    sample_app_welcome = '//*[@id="loginstatus"]'

    # Text Input
    text_input_link = '//a[contains(@href,"/textinput")]'
    text_input_name = '//input[@id="newButtonName"]'
    text_input_btn = '//button[@id="updatingButton"]'

    # Dynamic Table
    dynamic_table_link = '//a[contains(@href,"/dynamictable")]'
    dynamic_table_headers = '//span[@role="columnheader"]'
    dynamic_table_cells = '//span[@role="cell"]'
    dynamic_table_yellow = '//*[@class="bg-warning"]'

    # Dynamic ID
    dynamic_id_link = '//a[contains(@href,"/dynamicid")]'
    dynamic_id_btn = '//button[@class="btn btn-primary"]'

    # Class Attribute
    class_attr_link = '//a[contains(@href,"/classattr")]'
    class_attr_btn = '//*[contains(@class," btn-primary btn-test")]'

    # Load Delay
    load_delay_link = '//a[contains(@href,"/loaddelay")]'
    load_delay_btn = '//button[@class="btn btn-primary"]'

    # Progress Bar
    progress_bar_link = '//a[contains(@href,"/progressbar")]'
    progress_bar_start = '//button[@id="startButton"]'
    progress_bar_stop = '//button[@id="stopButton"]'
    progress_bar_bar = '//div[@id="progressBar"]'
    progress_bar_result = '//p[@id="result"]'

    # Scrollbars
    scrollbars_link = '//a[contains(@href,"/scrollbars")]'
    scrollbars_btn = '//button[@id="hidingButton"]'

    # Non-Breaking Space
    nbsp_link = '//a[contains(@href,"/nbsp")]'
    nbsp_btn = '//button[text()="My\u00A0Button"]'

    # Overlapped Element
    overlapped_link = '//a[contains(@href,"/overlapped")]'
    overlapped_name = '//input[@id="name"]'

    # Visibility
    visibility_link = '//a[contains(@href,"/visibility")]'
    visibility_hide_btn = '//button[@id="hideButton"]'
    visibility_removed_btn = '//button[@id="removedButton"]'
    visibility_zero_width_btn = '//button[@id="zeroWidthButton"]'
    visibility_overlapped_btn = '//button[@id="overlappedButton"]'
    visibility_opacity_0_btn = '//button[@id="transparentButton"]'
    visibility_hidden_btn = '//button[@id="invisibleButton"]'
    visibility_display_none_btn = '//button[@id="notdisplayedButton"]'
    visibility_offscreen_btn = '//button[@id="offscreenButton"]'

    # Client Side Delay
    clientdelay_link = '//a[contains(@href,"/clientdelay")]'
    clientdelay_btn = '//button[@id="ajaxButton"]'
    clientdelay_spinner = '//i[@id="spinner"]'
    clientdelay_text = '//p[@class="bg-success"]'

    # AJAX Data
    ajax_link = '//a[contains(@href,"/ajax")]'
    ajax_btn = '//button[@id="ajaxButton"]'
    ajax_text = '//p[@class="bg-success"]'
