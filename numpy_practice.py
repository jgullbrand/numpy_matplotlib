"""4 critics reviewed 50 movies from 1-5"""
import numpy as np
from matplotlib import pyplot as plt

#Creates an array from the data in the file
movie_ratings = np.genfromtxt('movie_ratings.csv', delimiter = ',')
#print(movie_ratings)

#convert the full list of movie rating to be out of 100 rather than out of 5. 4/5 => 80/100
hundred_scale_ratings = movie_ratings * 20
#print(hundred_scale_ratings)

critic_one_ratings = hundred_scale_ratings[:,0]
critic_two_ratings = hundred_scale_ratings[:,1]
critic_three_ratings = hundred_scale_ratings[:,2]
critic_four_ratings = hundred_scale_ratings[:,3]

total_rating_avg = (critic_one_ratings + critic_two_ratings + critic_three_ratings + critic_four_ratings) / 4.
#print(total_rating_avg)

#print & view specific columns of reviews for each critic.
def print_critic_results(column_num):
	print("Full review results from critic #{}".format(column_num+1))
	print(hundred_scale_ratings[:,column_num])

def get_high_ratings():
	print("Percentage of reviews over 80:")
	print(np.mean(hundred_scale_ratings > 80))

#get_high_ratings()

avg_rating = np.mean(hundred_scale_ratings)
median_rating = np.median(hundred_scale_ratings)
first_quartile = np.percentile(hundred_scale_ratings, 25)
third_quartile = np.percentile(hundred_scale_ratings, 75)
interquartile_range = third_quartile - first_quartile
std_ratings = np.std(hundred_scale_ratings)
#axis = 0 looks at columns. axis = 1 looks at rows
avg_rating_per_critic = np.mean(hundred_scale_ratings, axis =0)
sorted_reviews_critc_one = np.sort(hundred_scale_ratings[:,0])

#plots a histogram of the data
plt.hist(total_rating_avg, bins =10, range = (20,100)) #data is only available between 20-100
plt.title('Avg Movie Ratings for 50 Movies by four critics')
plt.xlabel('Avg rating out of 100')
plt.ylabel('# movies')
plt.show()

