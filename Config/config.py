class TestData:
    """En esta clase se almacenan data para los tests (url, user, pass)"""

    browser = 'Chrome'
    base_url = 'http://uitestingplayground.com'

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