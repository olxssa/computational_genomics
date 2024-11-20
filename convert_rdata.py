import pandas as pd
import rdata

r_data = rdata.parser.parse_file("/Users/olyssa/Downloads/compGenomRData-1-2.0/inst/extdata/leukemiaExpressionSubset.rds")

# %%
as_dict = rdata.conversion.convert(r_data)
df = pd.DataFrame(as_dict)