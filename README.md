
The main purpose of the bot is to limit the number of messages in chat rooms to avoid spamming 

How to start:

pip install - r requirements.txt


Enter your data in the cfg.sample.yml file, which contains basic parameters such as:
<i>
- bot token 
- group ID 
- Telegram admin id</i> 

and other settings to connect to MySQL database

![paint1.png](https://github.com/cutcutcute/PythonChatBot/blob/main/images/paint1.png)

<b>Add the bot to your group and assign it as an administrator</b>

![1 (1).gif](https://github.com/cutcutcute/PythonChatBot/blob/main/images/1%20(1).gif)

<b>start -> python main.py</b>

You can change both general settings and personal settings for each user you add


<b>General Settings</b>

- Message limit
- Time for which messages will be calculated 
- The message that the user will see when the limit is exceeded 

 (<i>When setting this parameter you can use such tags as <b>$user</b> - will display the user name <b>$limit</b> - will specify the message limit <b>$hours</b> - will tell the user about the available time period</i>).
- Message display time

<b>Personal settings</b>

Here you can configure permissions for each user separately. If a user has status 1 - no restrictions are imposed on him until you change his status, If you want to give access to a user for a certain period of time you can do it by setting the time period in the personal settings

You can also add a comment for a specific user that only you will see

![video5273957472820803010.gif](https://github.com/cutcutcute/PythonChatBot/blob/main/images/video5273957472820803010.gif)

A user who does not have access to this bot can keep in touch with the administrator by writing to the bot in a private message. In the meantime, the administrator will see the notification and can reply to the user by specifying his id via <i>@</i>

![video5273957472820803054.gif](https://github.com/cutcutcute/PythonChatBot/blob/main/images/video5273957472820803054.gif)
