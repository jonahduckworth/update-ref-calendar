# update-ref-calendar

```
update google calendar with games posted on GOALLINE
```

## GOALLINE User Interface
<img width="1440" alt="Screenshot 2023-01-05 at 10 40 22 AM" src="https://user-images.githubusercontent.com/35585020/210847081-28ce3142-393f-4653-b9a2-8b88784af6d8.png">

## Phone Calendar App After Running Program

![IMG_0152](https://user-images.githubusercontent.com/35585020/210847478-0e31da69-b35b-4aca-96f0-e7bfa37aa044.PNG)

![IMG_0153](https://user-images.githubusercontent.com/35585020/210847951-1b24a867-848e-4a1b-92a5-22d9b4f95352.jpeg)

## Preparation

#### Clone Repo

- Open a terminal window.
- Navigate to the directory where you want to clone the repository.
- Run the following command:

        git clone git@github.com:jonahduckworth/update-ref-calendar.git

  This will create a new directory named `update-ref-calendar`, and clone the repository files into it.
  
#### Get GOALLINE Data
  
- Go to [GOALLINE](https://czrc.goalline.ca/show_referee_assignments.php)
- Ensure that you are logged in
- In the browser, go to developer tools and click the `Network` tab
- Refresh the page
- Right click show_referee_assignments.php, hover over copy, and then copy as cURL. Like this:

<img width="1440" alt="Screenshot 2023-01-05 at 10 28 00 AM" src="https://user-images.githubusercontent.com/35585020/210843053-f8537353-6d7f-4602-a81b-ed85016f65f9.png">

#### Convert cURL into Python Requests

- Go to [this website](https://curlconverter.com/) to convert cURL

#### Insert Python Requests into Code

- In src/config.py, add the cookies, headers, and data objects that were converted from cURL

## Run Program

- cd src
- Run:

       pip install -r requirements.txt

- Run:

       python3 update_calendar.py
       
       
