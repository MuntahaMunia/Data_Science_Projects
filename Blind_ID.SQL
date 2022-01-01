USE [Database_name]
GO
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER FUNCTION [Function_name].[Column_name]
    (
	      @columnName as NVARCHAR(255)
	)
RETURNS NVARCHAR(255)
AS
BEGIN
    Declare
	@Output NVARCHAR(255),
	@TotalLength INT,
	@LoopCounter INT = 1;
	
	SET @TotalLength = LEN(@columnName)
	WHILE @LoopCounter <= @TotalLength
	BEGIN
	 SET @Output =
	 CONCAT (@Output,
	      CASE SUBSTRING (@columnName, @LoopCounter, 1)
		      WHEN '1' THEN '5'
			  WHEN '2' THEN '4'
			  WHEN '3' THEN '6'
			  WHEN '4' THEN '8'
			  WHEN '5' THEN '9'
			  WHEN '6' THEN '0'
			  WHEN '7' THEN '1'
			  WHEN '8' THEN '2'
			  WHEN '9' THEN '3'
			  WHEN '0' THEN '7'
			  WHEN 'A' THEN 'M'
			  WHEN 'B' THEN 'N'
			  WHEN 'C' THEN 'O'
			  WHEN 'D' THEN 'P'
			  WHEN 'E' THEN 'Q'
			  WHEN 'F' THEN 'R'
			  WHEN 'G' THEN 'S'
			  WHEN 'H' THEN 'T'
			  WHEN 'I' THEN 'W'
			  WHEN 'J' THEN 'X'
			  WHEN 'K' THEN 'Y'
			  WHEN 'L' THEN 'Z'
			  WHEN 'M' THEN 'A'
			  WHEN 'N' THEN 'B'
			  WHEN 'O' THEN 'C'
			  WHEN 'P' THEN 'D'
			  WHEN 'Q' THEN 'E'
			  WHEN 'R' THEN 'F'
			  WHEN 'S' THEN 'G'
			  WHEN 'T' THEN 'G'
			  WHEN 'U' THEN 'V'
			  WHEN 'V' THEN '4'
			  WHEN 'W' THEN 'U'
			  WHEN 'X' THEN 'I'
			  WHEN 'Y' THEN 'L'
			  WHEN 'Z' THEN 'K'
			  ELSE ''
		END)
	SET @LoopCounter = @LoopCounter + 1
	END
 RETURN @OutPut
END


