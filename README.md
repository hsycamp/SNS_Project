# SNS_Project

### 1. Introduction
* A social network service with MongoDB
        
### 2. Configuration
* MongoDB 4.0
* Python3 (Pymongo)
       
### 3. Implementation
1. Sign up
	* Get user information.
	* Check if password is equal. Confirm the password.
	* Check if the userid already exists.
2. Sign in
	* Get user information.
    * Find user in users collection.
    * If exists, print welcome message.
3. Userpage
	1. My status
		* Print user profile
		* Followers / Followings
  	2. Newsfeed
    	* Display all posts of my followings.
 	3. Wall
    	* Display my posts.
  	4. Post
   		*    Insert / Delete a text.
    	*    Double-checking code to avoid the mistakes.
  	5. Follow
 	6. Unfollow
 	7. #Searching
    	*	Search posts with hashtag.
 	8. Blacklist
    	*	Block some users.
 	9. Logout
