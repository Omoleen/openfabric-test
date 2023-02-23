# NLP Chatbot about Science
This is the answer to the task given to create an NLP chatbot about science. After considering different options, I decided to build a question and answering chatbot model. To do so, I used datasets from Science Question Answering (ScienceQA) and Textbook Question Answering (TQA). Although I gathered 30,000+ questions and answers from these sources, I had to clean the dataset due to the presence of images and questions that required options. In the end, I was left with a total of 16,504 questions, which I used for the NLP chatbot.

The datasets used and the code used to clean them are available in the Datasets folder. The cleaned dataset that was used for the chatbot is available as total.csv. The chatbot code is available in chatbot.py.

To calculate the similarity between the questions asked to the questions in my dataset, I used TDIFVectorizer and cosine similarity.

# Screenshots:

![alt text](https://github.com/Omoleen/openfabric-test/blob/master/Screenshot%202023-02-23%20at%2011.00.17%20PM.png)

![alt text](https://github.com/Omoleen/openfabric-test/blob/master/Screenshot%202023-02-23%20at%2011.00.46%20PM.png)

![alt text](https://github.com/Omoleen/openfabric-test/blob/master/Screenshot%202023-02-23%20at%2011.01.20%20PM.png)

![alt text](https://github.com/Omoleen/openfabric-test/blob/master/Screenshot%202023-02-23%20at%2011.01.58%20PM.png)

# Citations

Kembhavi, A., Seo, M., Schwenk, D., Choi, J., Farhadi, A., & Hajishirzi, H. (2017). Are You Smarter Than A Sixth Grader? Textbook Question Answering for Multimodal Machine Comprehension. In Conference on Computer Vision and Pattern Recognition (CVPR).

Lu, P., Mishra, S., Xia, T., Qiu, L., Chang, K.-W., Zhu, S.-C., Tafjord, O., Clark, P., & Kalyan, A. (2022). Learn to Explain: Multimodal Reasoning via Thought Chains for Science Question Answering. In The 36th Conference on Neural Information Processing Systems (NeurIPS).



