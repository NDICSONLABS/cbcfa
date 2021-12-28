# # # -*- coding: utf-8 -*-
# # """
# # Created on Mon Dec 27 20:53:50 2021

# # @author: the eye informatique

# # GDrive_Client_id = '1017494936870-9nl5v20dqacoe76l2v1klcntlkatfpuk.apps.googleusercontent.com'
# # """

# # import the required libraries
from __future__ import print_function
import pickle
import os.path
import io
import shutil
import requests
import pprint
from mimetypes import MimeTypes
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload

s=requests.Session()

resp = s.get("https://drive.google.com/drive/folders/1na6yGjYI6wbuhWaAZIFDxsH2l7-plfuS?usp=sharing")
pprint.pprint(resp.text)

# file_id = '0BwwA4oUTeiV1UVNwOHItT0xfa2M'
# request = drive_service.files().get_media(fileId=file_id)
# fh = io.BytesIO()
# downloader = MediaIoBaseDownload(fh, request)
# done = False
# while done is False:
#     status, done = downloader.next_chunk()
#     print "Download %d%%." % int(status.progress() * 100)
# if done:
#     with open(r"E:\Development\projects\web\falist\faform\testdownload\newfile2.xlsx",'wb') as fd:
#         fd.write(fh)

# class DriveAPI:
# 	global SCOPES
# 	
# 	# Define the scopes
# 	SCOPES = ['https://www.googleapis.com/auth/drive']

# 	def __init__(self):
# 		
# 		# Variable self.creds will
# 		# store the user access token.
# 		# If no valid token found
# 		# we will create one.
# 		self.creds = None

# 		# The file token.pickle stores the
# 		# user's access and refresh tokens. It is
# 		# created automatically when the authorization
# 		# flow completes for the first time.

# 		# Check if file token.pickle exists
# 		if os.path.exists('token.pickle'):

# 			# Read the token from the file and
# 			# store it in the variable self.creds
# 			with open('token.pickle', 'rb') as token:
# 				self.creds = pickle.load(token)

# 		# If no valid credentials are available,
# 		# request the user to log in.
# 		if not self.creds or not self.creds.valid:

# 			# If token is expired, it will be refreshed,
# 			# else, we will request a new one.
# 			if self.creds and self.creds.expired and self.creds.refresh_token:
# 				self.creds.refresh(Request())
# 			else:
# 				flow = InstalledAppFlow.from_client_secrets_file(
# 					'credentials.json', SCOPES)
# 				self.creds = flow.run_local_server(port=0)

# 			# Save the access token in token.pickle
# 			# file for future usage
# 			with open('token.pickle', 'wb') as token:
# 				pickle.dump(self.creds, token)

# 		# Connect to the API service
# 		self.service = build('drive', 'v3', credentials=self.creds)

# 		# request a list of first N files or
# 		# folders with name and id from the API.
# 		results = self.service.files().list(
# 			pageSize=100, fields="files(id, name)").execute()
# 		items = results.get('files', [])

# 		# print a list of files

# 		print("Here's a list of files: \n")
# 		print(*items, sep="\n", end="\n\n")

# 	def FileDownload(self, file_id, file_name):
# 		request = self.service.files().get_media(fileId=file_id)
# 		fh = io.BytesIO()
# 		
# 		# Initialise a downloader object to download the file
# 		downloader = MediaIoBaseDownload(fh, request, chunksize=204800)
# 		done = False

# 		try:
# 			# Download the data in chunks
# 			while not done:
# 				status, done = downloader.next_chunk()

# 			fh.seek(0)
# 			
# 			# Write the received data to the file
# 			with open(file_name, 'wb') as f:
# 				shutil.copyfileobj(fh, f)

# 			print("File Downloaded")
# 			# Return True if file Downloaded successfully
# 			return True
# 		except:
# 			
# 			# Return False if something went wrong
# 			print("Something went wrong.")
# 			return False

# 	def FileUpload(self, filepath):
# 		
# 		# Extract the file name out of the file path
# 		name = filepath.split('/')[-1]
# 		
# 		# Find the MimeType of the file
# 		mimetype = MimeTypes().guess_type(name)[0]
# 		
# 		# create file metadata
# 		file_metadata = {'name': name}

# 		try:
# 			media = MediaFileUpload(filepath, mimetype=mimetype)
# 			
# 			# Create a new file in the Drive storage
# 			file = self.service.files().create(
# 				body=file_metadata, media_body=media, fields='id').execute()
# 			
# 			print("File Uploaded.")
# 		
# 		except:
# 			
# 			# Raise UploadError if file is not uploaded.
# 			raise UploadError("Can't Upload File.")

# if __name__ == "__main__":
# 	obj = DriveAPI()
# 	i = int(input('''"Enter your choice:
# 				"1 - Download file, 2- Upload File, 3- Exit.\n"'''))
# 	
# 	if i == 1:
# 		f_id = input("Enter file id: ")
# 		f_name = input("Enter file name: ")
# 		obj.FileDownload(f_id, f_name)
# 		
# 	elif i == 2:
# 		f_path = input("Enter full file path: ")
# 		obj.FileUpload(f_path)
# 	
# 	else:
# 		exit()



# # import requests

# # def download_file_from_google_drive(id, destination):
# #     URL = "https://docs.google.com/spreadsheets/d/1ct1BrCwisybOYhJIi3eij2xQh-dHGL3t/edit?usp=drivesdk&ouid=110274313920282607548&rtpof=true&sd=truehttps://docs.google.com/spreadsheets/d/1ct1BrCwisybOYhJIi3eij2xQh-dHGL3t/edit?usp=drivesdk&ouid=110274313920282607548&rtpof=true&sd=true"

# #     session = requests.Session()

# #     response = session.get(URL, stream = True)
# #     token = get_confirm_token(response)

# #     if token:
# #         params = { 'id' : id, 'confirm' : token }
# #         response = session.get(URL, stream = True)

# #     save_response_content(response, destination)    

# # def get_confirm_token(response):
# #     for key, value in response.cookies.items():
# #         if key.startswith('download_warning'):
# #             return value

# #     return None

# # def save_response_content(response, destination):
# #     CHUNK_SIZE = 32768

# #     with open(destination, "wb") as f:
# #         for chunk in response.iter_content(CHUNK_SIZE):
# #             if chunk: # filter out keep-alive new chunks
# #                 f.write(chunk)

# # if __name__ == "__main__":
# #     file_id = "1iI5DnSlydRvLZLwLueZZ8_JmYPav0Eq_"
# #     destination = r"E:\Development\projects\web\falist\faform\testdownload\file2.xlsx"
# #     download_file_from_google_drive(file_id, destination)