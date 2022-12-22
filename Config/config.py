class TestData:
    """This class stores data for the tests"""

    browser = 'Chrome'
    base_url = 'http://uitestingplayground.com'
    base_url_ssl = 'https://uitestingplayground.com'

    # Sample App
    sample_app_login_data = [
        ('Roberto', 'pwd', 'Welcome, Roberto!'),
        ('', 'pwd', 'Invalid username/password'),
        ('Roberto', 'asd', 'Invalid username/password'),
        ('', '', 'Invalid username/password'),
        ('', 'asd', 'Invalid username/password'),
        ('Roberto', '', 'Invalid username/password'),
    ]

    # Text Input
    text_input_field_data = [
        ('Roberto', 'Roberto'),
        ('@ !', '@ !'),
        (' ', ''),
        ('', 'Button That Should Change it\'s Name Based on Input Value'),
    ]

    # Progress Bar
    progress_bar_result = '0'

    # Overlapped Element
    overlapped_name = 'Roberto'

    # Client Side Delay
    clientdelay_data = 'Data calculated on the client side.'

    # AJAX Data
    ajax_data = 'Data loaded with AJAX get request.'

    # Mouse Over
    mouseover_data = [(0, '0'), (1, '1'), (2, '2'), (34, '34'), (101, '101')]

    # Verify Text
    verifytext_expected = 'Welcome UserName!'

    # Click
    click_class_before_expected = 'btn btn-primary'
    click_class_after_expected = 'btn btn-success'
