Detailed explanation on how I have creted this mini project and also how to run it 

Basically Project is divided into 3 parts :
=======================================================================================================================

1. TASK-A : Project Setup And Basic UI

Step-1 : I have created a new folder named "MiniProject_Charmi"
Step-2 : Then in that same folder i have created a virtual environment
        as i am using windows : python -m venv env
        writing this in cmd will create a new folder named "env" in the same folder

Step-3 : Then I have activated the virtual environment by writing the following command in cmd
        for windows : env\Scripts\activate
Step-4 : Then I have installed the required libraries by writing the following command in cmd
        As for the UI Framework I have used Streamlit
        syntax : pip install streamlit
Step-5 : Then I have created a new python file named "main.py" in the same folder
Step-6 : Then I have written the basic UI code in the main.py file 
Step-7 : Then I have run the main.py file by writing the following command in cmd
        syntax : streamlit run main.py

Then the purpose of this project is to create a simple UI where user can input there current mood and when he/she click on the suggest playlist button then it will display the playlist based on the user's mood, and also a vibe card will be displayed and also changes the background color according to the mood.
After that if user want to listen the playlist then on clicking the play button it will open the playlist in the window media player and that playlist will get automatically searched in the windows media player.

=======================================================================================================================

2. TASK-B : AI/ML Integration

For this task I have used the following libraries :
1. transformers 
2. torch

syntax : pip install transformers torch 

Model : I have use Hugging face sentiment-analysis model for my miniproject

--> Model that I have used : sentiment-analysis ,distilbert-base-uncased-finetuned-sst-2-english
Now when the user clicks on the suggest playlist button then he/she gets the playlist according to the mood that means if user types 'i am happy' then happy word is fetched and using sentiment-analysis model it will show wheather it is positive or negative and on basis of that the playsist will be shown.
And also according to the requirement the output is shown in the UI part when user clicks on the button whicever the playlist has been generated on the basis of the positive or negative sentiment result it is shown there in the UI part.

So this is the backend where the model is used to get the playlist according to the user's mood, and i have integrated it with the task-A for the UI part.


=======================================================================================================================

3. TASK-C : Automation

For automation I have used the pyautogui library
syntax : pip install pyautogui

Now for the automation part i have integrated this with the Task-A and Task-B part so when user has already clicked on the button of suggestmplaylist at that time playlist was generated now, in if the user want to listen that playlist then there is a button also available in the UI part, when user clicks on that button then it will open the playlist in the windows media player automatically

So in backend using the pyautogui library i am able to do this automation part,
now firstly when the playlist is already suggest wsing the sentiment analysis model ,then the user can click on the button to listen the playlist and then the with the help of pyautogui firstly the windows media player will be open and that will be opened using windows+r and there it will automatically typed wmplayer (a shortcut to open windows media player) then in seconds it will maximize the screen if it is minimized while opening bcz for searching the pointer is set at a particular point so if it is minimized then it will not be able to search the playlist in the windows media player, after that that generated playlist is searched in the windows media player.

