# Computer Science Projects - Portfolio Project: Recommendation Software

This portfolio project was created as part of [Codecademy's](https://www.codecademy.com) Computer Science Career Path course.

## Table of contents

- [Project Overview](#project-overview)
  - [Project objectives](#project-objectives)
- [Recommendation Software](#recommendation-software)
  - [Screenshots](#screenshots)
- [Process](#process)
  - [Flow chart](#flow-chart)
  - [Coding decisions](#coding-decisions)
  - [What I learned](#what-i-learned)
  - [Potential improvements to program](#potential-improvements-to-program)
  - [Useful resources](#useful-resources)
- [Author](#author)

## Project Overview

"In this portfolio project, you will research, brainstorm, and build a basic recommendation program for a topic of your choice. By entering letters or words into the terminal, the program will suggest a specific category for the user to explore. If the user is interested in the category, the program will provide a variety of related recommendations to the user. After you finish building the program, you will create a blog post to share the program on a publication of your choice!" - [Codecademy](https://www.codecademy.com)

### Project objectives

- Store data in a data structure.
- Use an algorithm to sort or search for data within a data structure.
- Use Git version control.
- Use the command line and file navigation.
- Write a technical blog post on the project.

## Recommendation Software

For this particular project I decided to create recommendation software for UK TV shows.

- Solution URL: [Recommendations](./recommendations.py)

### Screenshots

#### Instructions:

![Instructions for how to use the recommendation software]() TODO

#### Number of recommendations for selected genre:

![Number of recommendations for genre/category]() TODO

#### Filtered recommendations for multiple genres:

![Filter recommendations by multiple genres/categories]() TODO

## Process

- Think of an idea for the type of recommendation software that I want to build - what topic will it be focused on.
- Project brainstorming on how the recommendation software will work:

  - Recommendation software to be based on recommending UK TV shows by genres.
  - Import [dictionary of data](./data.py) where keys are TV shows and values are the TV show's genre(s).
  - Import Node and Stack classes as stack to be used to contain the selected genres that will filter the TV shows.
  - Display instructions of how to use the recommendation software.
  - START:
    - Get initial letter for genre type from user and check if any genres match initial letter:
      - If no, ask user for a different initial letter.
      - If yes, display list of matching genre names.
    - Ask user whether wish to choose genre from matching genre names:
      - If no, ask user for a different initial letter.
      - If yes, is there is only one matching genre?
        - If yes, add genre to stack to filter TV shows by that genre.
        - If no, get initial letters (minimum 2) from user and check if that matches any from the genre list already generated.
          - If no, ask user to enter letters again to match genre from genre list.
          - If yes, add genre to stack to filter TV shows by that genre.
    - Is number of TV shows that match the chosen genre = 0?
      - If yes, is number of genres used to filter > 1?
        - If no, then should state error as should have shows to show for a single genre.
        - If yes, remove last genre from stack and refilter by genres left in stack and continue with the following if no below.
      - If no, is number of TV shows <= 5?
        - If yes, display TV show recommendations based off selected genres and ask user whether wish to choose another genre to filter the recommendations further.
          - If yes, go back to get another genre.
          - If no, display number of TV show recommendations that match the selected genres.
        - If no, display number of TV show recommendations that match the selected genres.
    - Ask user whether wish to get another TV show recommendation?
      - If yes, RESTART.
      - If no, END.

- Set up a GitHub repository.
- Set up Git version control.
- Use ChatGPT to help create data for UK TV shows and their genres.
- Write recommendation software program.
- Refactor program.
  - Initial refactoring to make code more concise.
  - Structural changes that would improve efficiency/scalability/useability etc.
  - Add own quicksort algorithm.
- Create blog post about project. (This README file is my post about the project I have created.)

### Flow chart

![Flowchart of how software recommendation program works](./img/TV-shows-flowchart.jpg)

### Coding decisions

There are a number of decisions I made as to how to approach and code this recommendation software. So below is an explanation as to the what and why I wrote the code in the way that I did.

- When creating the original flowchart for describing the basic structure of how I wanted the program to work, a stack to contain the selected genres used to filter the TV shows would be needed.

- I've primarily used inbuilt Python functions for efficiency, however, I have implemented my own Stack/Node class and where I originally used the inbuilt Python `sorted()` function I have replaced that with my own quicksort algorithm. `sorted()` is likely to be more efficient than my own sort function, however, as one of the project objectives was to write your own algorithm then it seemed appropriate to use that here.

- Error checking is done for validating all user input:

  - Y/N answer responses
  - Initial letter search of genre names
  - Letters to confirm genre selection

- Upon initial completion and refactoring, I realised that the way the data was formatted in the dictionary was not optimal coding wise. The dictionary containing the UK TV shows data, had the titles of TV shows as the keys, and the genres as the values. However, given obtaining recommendations is based of the genres, it made more sense to have a dictionary with the genres as keys and TV shows as values.

  - As the original dictionary format was much more readable from a human perspective and easier for a human to add more data to (single line in dictionary per TV show) I decided to keep it and add extra functions and code to create a json file with the data in a dictionary with keys as genres and TV show titles as values. This code was placed in a separate file [create_json_data.py](./create_json_data.py) so that it could be run separately outside the main program to generate the json file of data that can then be imported into [recommendations.py](./recommendations.py) I deliberately used more generic naming so that it's possible to reuse with different data content (so long as data is stored in a dictionary in the same format).

  ```python
  import json
  from data import data_dict

  def transform_dict(dictionary):
      data_in_categories = {}
      for item, categories in dictionary.items():
          categories_list = categories.split(", ")
          for category in categories_list:
              if category not in data_in_categories:
                  data_in_categories[category] = []
              data_in_categories[category].append(item)
      return data_in_categories

  def save_transformed_dict(file_path, transformed_dict):
      with open(file_path, "w") as json_file:
          json.dump(transformed_dict, json_file, indent=4)

  transformed_dict = transform_dict(data_dict)
  save_transformed_dict("data.json", transformed_dict)
  ```

- I also chose to overhaul the naming of variables and functions to more generic names within the recommendation program, so that the program can be used with other datasets that are not UK TV shows, so long as they adhere to the data format required in [data.py](./data.py). (Change contents of variables according to data, e.g. if recommendations on restaurants, `data_items = "restaurant"`, `data_categories = "cuisine style"`, `data_dict = { "Restaurant Name": "cuisine_style" }`)

  ```python
  data_items = "UK TV shows"
  data_categories = "genre"
  data_dict = {
    "UK TV show title": "Genre_1, Genre_2, Genre_3"
  }
  ```

### What I learned

- I learned about how to use set intersections and `intersection_update` to improve efficiency of filtering of data for different genres.

  ```python
  if current_category_value in items_in_categories:
    current_items = set(items_in_categories[current_category_value])

    if recommendations is None:
      recommendations = current_items
    else:
      recommendations.intersection_update(current_items)
  ```

### Potential improvements to program

- Allow the user to select a single recommendation item to display further information about it:

  - Add option to choose a single recommendation item.
  - Change dataset to allow more information e.g. for UK TV shows, further information could be date/time/channel when showing etc or a brief synopsis of the show.
  - Be able to extract further information to show from dataset.

- When using more than one category to filter data that results in zero results, rather than removing the last category to allow for showing results, allow the user to remove a category of their choice instead.
  - Add option to select category to remove from filter.
  - Change data structure used for selected categories from a stack to a linked list.

### Useful resources

- [ChatGPT](https://chatgpt.com/)

## Author

- V. Tickner
