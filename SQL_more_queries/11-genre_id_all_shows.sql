-- List all TV shows with their genre_id, including shows with no genre  

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows, tv_show_genres
WHERE tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
