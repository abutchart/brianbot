# brianbot
GPT-2 Discord bot trained on my chat messages. Can be trained to mimic other people as well.

![image](https://user-images.githubusercontent.com/54566106/132962466-c615f3bf-cf0f-4ecd-8833-6b55c64f82f3.png)

## Dependencies
Note: this bot uses tensorflow 1.15, which is incompatable with Python 3.8. Use Python 3.7 instead.

Install the packages with:

`pip install -r requirements.txt`

## Usage
I decided to remove my personal trained model from this repo to protect the privacy of people I have talked with that the bot likes to name-drop every now and then. To train and use your own model, perform the following steps:

1. Download your discord messages using https://github.com/Tyrrrz/DiscordChatExporter. Select the channels you want to download and export as csv.
2. Add your dataset folder path (the folder with all your .csv's) and your output file path to preprocessing.py. Run preprocessing.py.
3. Follow the instructions in https://colab.research.google.com/github/sarthakmalik/GPT2.Training.Google.Colaboratory/blob/master/Train_a_GPT_2_Text_Generating_Model_w_GPU.ipynb to train your model. Under "Uploading a Text File to be Trained to Colaboratory", upload the .txt output from preprocessing.py. Once GPT-2 is retrained, download it to your computer and put the finished model in the checkpoints folder.
4. Do you have any emojis/images/links you send frequently? Put them in the corresponding emojis.txt, images.txt, and links.txt files. Emojis should be formatted like :emojiname:. Links to images should be put in images.txt, not actual images.
5. Add your bot token and id to bot.py.
6. Done! Add the bot to your server in the usual fashion.
