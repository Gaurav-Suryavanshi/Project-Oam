from openai import OpenAI

client = OpenAI(api_key = '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')
response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt="write an email to HR for sick leave in a professional manner",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)

#choices=[CompletionChoice(finish_reason='length', index=0, logprobs=None, text="\n\nSubject: Request for Sick Leave\n\nDear [HR Manager's Name],\n\nI am writing this email to inform you that I will not be able to come to work today, [Date], as I am feeling unwell. Therefore, I would like to request a sick leave for the day.\n\nI woke up this morning with [mention your symptoms] and I understand the importance of being present at work, but due to my current health condition, I will not be able to perform my duties effectively. I have consulted with my doctor and have been advised to take rest and medication for the day.\n\nI have completed all my pending tasks and have informed my team about my absence. I have also informed my superior and have requested their support in case of any urgent matters that may arise in my absence.\n\nI will keep you updated regarding my health and expect to be back at work tomorrow, [Date]. In the meantime, if there is any specific procedure I need to follow for requesting a sick leave, please let me know. I will be available by phone or email in case of any urgent matters that require my attention.\n\nI apologize for any inconvenience this may cause and assure you that I will make up for any lost time upon my return. I have attached a copy of my doctor's")], created=1706875809, model='gpt-3.5-turbo-instruct', object='text_completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=256, prompt_tokens=12, total_tokens=268))