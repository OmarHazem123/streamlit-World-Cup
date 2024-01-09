import pandas as pmessi
import streamlit as stmessi
from style import add_background


def head () :
    stmessi.title("Qatar world cup 2022")
    stmessi.write("Book for the last dance \" *****France vs Argentina***** \" ")
    stmessi.image("https://media.cnn.com/api/v1/images/stellar/prod/231202112633-lionel-messi-world-cup-2022-file.jpg?c=16x9&q=h_653,w_1160,c_fill/f_webp")
    add_background()
def body () :
    name = stmessi.text_input("Enter your name")
    age = stmessi.number_input("Enter your Age", min_value=1)
    if age < 18:
        stmessi.write(" Come with your parents ")

    else:
        stmessi.write(" Come with your GF ")

    Country = stmessi.selectbox("Enter your country", [
        "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia",
        "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium",
        "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria",
        "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad",
        "Chile", "China", "Colombia", "Comoros", "Congo (Congo-Brazzaville)", "Costa Rica", "Croatia", "Cuba", "Cyprus",
        "Czechia (Czech Republic)", "Democratic Republic of the Congo (Congo-Kinshasa)", "Denmark", "Djibouti",
        "Dominica",
        "Dominican Republic", "East Timor (Timor-Leste)", "Ecuador", "Egypt",
        "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini (fmr. 'Swaziland')", "Ethiopia", "Fiji",
        "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala",
        "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Holy See", "Honduras", "Hungary", "Iceland", "India",
        "Indonesia",
        "Iran", "Iraq", "Ireland", "Italy", "Ivory Coast", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya",
        "Kiribati", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein",
        "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands",
        "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco",
        "Mozambique", "Myanmar (formerly Burma)", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand",
        "Nicaragua",
        "Niger", "Nigeria", "North Korea", "North Macedonia (formerly Macedonia)", "Norway", "Oman", "Pakistan",
        "Palau",
        "Palestine State", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal",
        "Qatar",
        "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines",
        "Samoa",
        "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone",
        "Singapore",
        "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Korea", "South Sudan", "Spain",
        "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Tajikistan", "Tanzania", "Thailand",
        "Togo",
        "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine",
        "United Arab Emirates",
        "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Vietnam", "Yemen",
        "Zambia", "Zimbabwe"
    ])
    Mobile_Number = stmessi.text_input("Enter your Mobile number")
    Fan_ID = stmessi.text_input(" Enter your Fan ID : ")
    blood_type = stmessi.radio("what's your blood type", ("+A", "-A", "+B", "-B", "+O", "-0"))
    if stmessi.button(" Book Now ! ") :
          if ( name == ""):
           stmessi.write (" **:red[ERROR !]** ")
          elif( Mobile_Number == "" ) :
              stmessi.write("**:red[ERROR !]**")
          elif (Fan_ID == "") :
              stmessi.write("**:red[ERROR !]**")
          else:
              stmessi.write(" we will contact with you")
              
add_background()
def sidbar () :
    stmessi.sidebar.title(" Qatar 2022 ")
    home = stmessi.sidebar.button("Home")
    Best_moument = stmessi.sidebar.button(" Best MOMENT  ")
    Best_goals = stmessi.sidebar.button(" Best Goals  ")
    Best_saves = stmessi.sidebar.button(" Best Saves  ")
    stadium = stmessi.sidebar.button(" Stadium  ")
    samole = stmessi.sidebar.button ( " Statstics ")
    HElp = stmessi.sidebar.button(" HELP  ")

    upload_National = stmessi.sidebar.file_uploader("Upload your National ID")

    if home:
        head()
        body()
    elif stadium :
        stmessi.title(" Lusail Stadium")
        stmessi.text("Lusail Stadium | Capacity: 80,000 seats | Opening: 2022")
        stmessi.image("https://www.stadiumguide.com/wp-content/uploads/lusail2022-1.jpg")
        stmessi.write("[Location](https://maps.app.goo.gl/k5xWY9GjjSFtvGZ26)")
        stmessi.text("Matches: \n- 5x Group Matches\n- 1x Round of 16\n- 1x Quarter-Final\n- 1x Semi-Final \n- Final")


        stmessi.title(" **Al Khor**")
        stmessi.text("Al Bayt Stadium | Capacity: 60,000 seats | Opening: 2021")
        stmessi.image("https://www.stadiumguide.com/wp-content/uploads/albayt_top.jpg")
        stmessi.write("[Location](https://maps.app.goo.gl/5MTsCDpNE9ffWALG9)")
        stmessi.text("Matches: \n- 5x Group Matches (incl. Opening Match)\n- 1x Round of 16\n- 1x Quarter-Final\n- 1x Semi-Final ")

        stmessi.title(" **Al Wakrah**")
        stmessi.text("Al Janoub Stadium | Capacity: 40,000 seats | Opening: 2019")
        stmessi.image("https://www.stadiumguide.com/wp-content/uploads/alwakrah_top.jpg")
        stmessi.write("[Location](https://maps.app.goo.gl/5voUofvVuB2iXUvR7)")
        stmessi.text("Matches: \n- 5x Group Matches \n- 1x Round of 16 ")

        stmessi.title(" **Al Rayyan**")
        stmessi.text("Ahmad Bin Ali Stadium | Capacity: 40,000 seats | Opening: 2020")
        stmessi.image("https://www.stadiumguide.com/wp-content/uploads/alrayyan_top.jpg")
        stmessi.write("[Location](https://maps.app.goo.gl/4e7mMcR95eoCAR4A8)")
        stmessi.text("Matches: \n- 5x Group Matches \n- 1x Round of 16 ")

        stmessi.title(" **Doha**")
        stmessi.text("Khalifa International Stadium | Capacity: 40,000 seats | Opening: 1976")
        stmessi.image("https://www.stadiumguide.com/wp-content/uploads/khalifanew_top.jpg")
        stmessi.write("[Location](https://maps.app.goo.gl/JTc3qCm1rRXz7b6S9)")
        stmessi.text("Matches: \n- 5x Group Matches \n- 1x Round of 16 \n- Match for Third Place")

        stmessi.title(" **Doha**")
        stmessi.text("Education City Stadium | Capacity: 40,000 seats | Opening: 2020")
        stmessi.image("https://www.stadiumguide.com/wp-content/uploads/qatarfoundation_top.jpg")
        stmessi.write("[Location](https://maps.app.goo.gl/hU8oDn6G9PdmVLir7)")
        stmessi.text("Matches: \n- 5x Group Matches \n- 1x Round of 16 \n- 1x Quarter-Final")

        stmessi.title(" **Doha**")
        stmessi.text("Stadium 974 | Capacity: 40,000 seats | Opening: 2021")
        stmessi.image("https://www.stadiumguide.com/wp-content/uploads/rasabuaboud2022.jpg")
        stmessi.write("[Location](https://maps.app.goo.gl/pR5mQbCwGLs5aJu96)")
        stmessi.text("Matches: \n- 5x Group Matches \n- 1x Round of 16 ")

        stmessi.title(" **Doha**")
        stmessi.text("Al Thumama Stadium | Capacity: 40,000 seats | Opening: 2021")
        stmessi.image("https://footballtripper.com/wp-content/uploads/al-thumama-stadium-aerial-856x380.jpg")
        stmessi.write("[Location](https://maps.app.goo.gl/E4LfYr5sPmJraWveA)")
        stmessi.text("Matches: \n- 5x Group Matches \n- 1x Round of 16 \n- 1x Quarter-Final ")
    elif Best_moument :
        stmessi.header(" :white[**BEST OF WORLD**]")
        stmessi.title("goal from another world from Salem el dosary in Argentina")
        stmessi.video("https://www.youtube.com/watch?v=YbjPGLSL8Vc")
        stmessi.title("unexpected qualified for Morocco")
        stmessi.video("https://www.youtube.com/watch?v=Kmb_3TWR2IY")
        stmessi.title("Messi finally won the world cup")
        stmessi.video("https://www.youtube.com/watch?v=IGjE_zgs2Hw")
    elif Best_goals :
        stmessi.header(" :white[**BEST OF GOALS**]")
        stmessi.title("Top 10 goals in Fifa world cup 2022")
        stmessi.video("https://www.youtube.com/watch?v=B95TJDnOJ_0")
    elif Best_saves:
        stmessi.header(" :white[**BEST OF SAVES**]")
        stmessi.title("incredible saves for keepers")
        stmessi.video("https://www.youtube.com/watch?v=HJKDjSURAx0")
    elif HElp :
        stmessi.header(" :white[**HOW I CAN UPLOAD NATIONAL ID**]")
        stmessi.write ("Certainly! To provide instructions on how to upload an ID, you'll need to specify the platform or service where the ID needs to be uploaded since the process can vary depending on the website, application, or organization. However, I can provide you with a general guide that you can customize based on the context. Let's assume you're referring to a typical online platform or account verification process:")
        stmessi.title(" Choose ")
        stmessi.image ("https://global.discourse-cdn.com/business7/uploads/streamlit/original/3X/6/c/6c8b4e12e47542ce7f3a5c11285d60ee597d4dfa.jpeg")
        stmessi.write("**that's how to upload your National ID**")
    elif samole :
        WC2024 = pmessi.read_csv("Messi.csv")
        stmessi.header(" All Data ")
        stmessi.write(WC2024.head(-1))

    else:
        head()
        body()
sidbar()
# Thank you All : )