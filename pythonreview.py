def create_youtube_video(title , description):
	Youtube = {"title" : title , "description" : description , "Likes" : 0 , "Dislikes" : 0 , "Comments" : {}}
	return Youtube


def likes(Youtube):
	if "Likes" in Youtube:
		Likes++
	else:
		print ("There is no key called Likes.")
	return Youtube



def dislikes(Youtube):
	if "Dislikes" in Youtube:
		Dislikes++
	else:
		print ("There is no key called Likes.")
	return Youtube


def add_comment(Youtube , username , comment_text):
	Comments["username"] = "comment_text"
	return Youtube


FirstYTV = create_youtube_video("IT2" , "Horror Movie")
print (FirstYTV)


