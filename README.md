# Django & Next.js(React)
The Django application scrapes data from [https://gogoflix.pro] and [https://fmoviesz.bz], while the Next.js (react) application renders the UI and use scraped data to search movies or tv shows

`Note: The [https://fmoviesz.to] is not accessible, change it to [https://fmoviesz.bz]`

### Requirement:
 - docker

### Installation:
 - Clone repository [https://github.com/jay-ong/task]
 - Next run the `run.sh`
    ```sh
    source run.sh
    ```
 - After running the `run.sh` it will show the id's of the django & react docker container
 - Now the Next.js(react-app) will run to http://localhost:3000 (No data yet)
 - Next to populate the scraped data from [https://gogoflix.pro] and [https://fmoviesz.bz], Go to http://localhost:8000/scraper (this will scrape the for the said URL's)
 - Last refresh the http://localhost:3000 , then you can now search for movies and tv shows
