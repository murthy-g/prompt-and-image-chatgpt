pre requisites

generate open api key using below
https://platform.openai.com/account/api-keys

run the below command in your terminal.

export OPEN_API_KEY=<< your open ai key >>

chmod 775 run.sh
./run.sh

pip install -r requirements.txt

run:

python main.py

This code generates a comprehensive explanation for the prompt you provide, regardless of the specific details, and it also generates an image based on the given prompt.

it uses text-davinci-003 model for generating the brief. also you can use DALL-E model for high quality images for the context




