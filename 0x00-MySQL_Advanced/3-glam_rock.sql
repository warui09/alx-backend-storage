-- lists all bands with Glam rock as their main style, ranked by their longevity

SELECT band_name, DATE_FORMAT(FROM_DAYS(DATEDIFF(COALESCE(split, "2022"), formed)), "%Y") as lifespan
WHERE style='Glam rock'
ORDER BY lifespan DESC;
