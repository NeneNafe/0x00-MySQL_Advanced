-- ranks country origins to bands, ordered by the number of fans
SELECT DISTINCT `origin`, SUM(`fans`) as `nb_fans` FROM `metal_bands`
GROUP BY `origin`
ORDER BY `nb_fans` DESC;
