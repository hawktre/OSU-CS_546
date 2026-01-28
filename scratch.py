import igraph as ig
import pandas as pd

#Read in the data
hsmetnet = pandas.read_csv(
    filepath_or_buffer= "https://csx46.s3-us-west-2.amazonaws.com/hsmetnet.txt", 
    sep='\t', 
    header=None,
    names= ["source", "target"])

#Drop Duplicates
hsmetnet.drop_duplicates(inplace=True)

#Print the first six rows 
hsmetnet.head(6)