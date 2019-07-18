/* Obtain some data (?) */

SET @fechaInicio = '2019-05-01 00:00:00';
SET @fechaFin = '2019-07-19 00:00:00';

SELECT from_unixtime(a.dateTime) `UTC`, a.dateTime, a.GA_Volt_o3 `Anapra_o3`, b.O3Ppm `Teledyne_o3` FROM
	(
		select
            Estacion28.archive.dateTime `dateTime`,
            Estacion28.archive.GA_Volt_o3
		from Estacion28.archive
	) as a
LEFT JOIN Teledyne.archive b ON a.dateTime = b.dateTime

where
	a.dateTime >= UNIX_TIMESTAMP(@fechaInicio) AND
	a.dateTime < UNIX_TIMESTAMP(@fechaFin)
    
UNION

SELECT from_unixtime(b.dateTime) `UTC`, b.dateTime, a.GA_Volt_o3 `Anapra_o3`, b.O3Ppm `Teledyne_o3` FROM
	(
		select
            Estacion28.archive.dateTime `dateTime`,
            Estacion28.archive.GA_Volt_o3
		from Estacion28.archive
	) as a
RIGHT JOIN Teledyne.archive b ON a.dateTime = b.dateTime

WHERE
	b.dateTime >= UNIX_TIMESTAMP(@fechaInicio) AND
	b.dateTime < UNIX_TIMESTAMP(@fechaFin)