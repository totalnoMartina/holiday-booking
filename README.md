# Holiday Booking Webiste - Holiday Home

This webpage is made for a privately owned house that rents out apartments to guests for summer holidays on the coastal side of Croatia. As clients have been using [Booking.com](https://www.booking.com/) for the past years, there has been some overlapping of bookings which were not easy to handle by the host. Through this website users can get into direct contact with the owner of the house and set up details of the booking process via email.

-- images of the website here

![HomePage](media/images/homepage-main.png?raw=true)

# Flowchart

# Features

## Existing features

A Navbar with contact number, names of the owners, an email address to contact the owners directly, Apartments images and description, a pricelist, a Calendar with available dates and prices per night, map with exact location and a weather widget for current weather informations
### The landing page image, contact number and nav

### The Apartments in offer with description, more images for the specific apartment

### The feedback from previous guests

### The booking system with calendar

### Admin login and features to upload new or change features of apartments

## Future features

* Being able to pay directly to the owners account
* Being able to receive a text message from the booking website when someone has an enquiry on booking the apartment/s


# Testing 

Most likely unittesting

- some examples of tests:
    - Check for availability of apartments
    - Check for booking more people than the apartments have rooms
    - Check for overlapping bookings - booking same apartment at same times by different user

## Validation testing, performance possibly

## Unfixed bugs

- TEXT COLOR CHANGE USING JINJA - On the 'Apartments' page, when customizing the decription text that is rendered using python jinja brackets, the text description was changing the color only in the first instance of the apartment 'Matea'. The other two apartments, had text in black which was not good UX. To fix this, and to make all three apartments render white text within bark-blue background, I went through administrator side and formatted the text using the options while inputting informations about the apartments. The best way for the admin to see the text written is while there, change background into darker color and before saving the information, just leave the text white and set background to transparent.

- MULTIPLE API'S USED ON A SINGLE PAGE - In the 'Holiday Home - About' page, there is a location widget for Google Maps, and also a weather widget for the current showcase of the weather in a specific location, and while all is working just fine, The console on the inspecting page, says that this case can cause troubles. I am still searching for the best solution, one of them was using 'iframe' so without the API but unfortunately, this did not render any map so I am looking into this.

- CAROUSEL FROM BOOTSTRAP 4.4 - The Carousel is working quite well and it contains the images that are rendered through Django using Jinja brackets, however, the first time the carousel renders and has the active class on and user is able to control only the first apartment image sliding. On a laptop, we can control the first carousel, and the second and third are automatically (seemingly) sliding. MOBILE - On my IPhone 6S, while checking images, using touch-screen, user is able to slide image on both sides, in every apartment instance.

# Deployment Steps

# Credits

- Description content was rendering including html markdown language so a filter called '|safe' was used to render the format properly, solution was found through [Stackoverflow](www.stackoverflow.com) and led me to [Django Documentation](https://docs.djangoproject.com/en/dev/ref/templates/builtins/?from=olddocs#safe)
## Content

- refer content - owner, booking.com

## Media

- Fonts from [Google Fonts](https://fonts.google.com/)
- refer owner, also booking.com
















