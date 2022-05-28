import tabula


def lambda_handler(event, context):
    cols = ["col1", "col2"]
    url = "https://github.com/tabulapdf/tabula-java/raw/master/src/test/resources/technology/tabula/arabic.pdf"
    pdf_df = tabula.read_pdf(url)
    df = pdf_df[0]
    df.columns = cols
    df.fillna('', inplace=True)
    return {"data": df.to_dict("records")}

if __name__ == "__main__":
    print(lambda_handler({}, {}))
