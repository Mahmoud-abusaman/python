SELECT countries.name, languages.language,languages.percentage
FROM countries join languages on countries.id=languages.country_id 
where languages.language="slovene"
order by percentage desc ;


2
select countries.name ,count(cities.id) as number_of_cities
 from countries join cities on countries.id=cities.country_id 
 group by country_id
 order by number_of_cities desc;


select cities.name,cities.population from countries join cities on countries.id=cities.country_id
where countries.name="mexico" and cities.population> 500000
order by cities.population desc;


select countries.name,languages.language,languages.percentage 
from countries join languages on countries.id=languages.country_id
where languages.percentage>89
order by languages.percentage desc;



SELECT name,surface_area,population FROM countries
where surface_area<501 
and population>100000;


SELECT * FROM world.countries 
where government_form like("%Constitutional Monarchy%") 
and capital>200 
and life_expectancy>75;

select cities.name,countries.name, district, cities.population
from cities join countries on countries.id=cities.country_id
where countries.name="Argentina" and cities.district="Buenos Aires" 
and cities.population>500000;


select  countries.region ,count(countries.id) As number_of_countries 
from countries group by region
order by number_of_countries desc;
