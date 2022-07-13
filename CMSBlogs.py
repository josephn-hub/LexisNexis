import psycopg2
import csv
import pandas as pd


class CmsBlogs(object):
    def __init__(self, hostname, port_id, database, username, path):
        self.path = path
        try:
            self.conn = psycopg2.connect(host=hostname,
                                         dbname=database,
                                         user=username,
                                         port=port_id)
            self.cur = self.conn.cursor()

        except Exception as error:
            print(error)

    def published_blogs(self):
        query = """select * from published_blogs"""
        header_list = ['Id', 'Name', 'Published_date', 'blog_Text', 'created_date']
        self.cur.execute(query)
        for record in self.cur.fetchall():
            with open(self.path + record[1] + "-" + record[4].strftime(
                    "%b") + "-" + "Published-blogs.csv", 'a') as f:
                writer = csv.writer(f)
                writer.writerow(record)

            df = pd.read_csv(self.path + record[1] + "-" + record[4].strftime(
            "%b") + "-" + "Published-blogs.csv", sep=",")
            df.drop_duplicates(subset=None, inplace=True)
            df.to_csv(self.path + record[1] + "-" + record[4].strftime(
                "%b") + "-" + "Published-blogs.csv", header=header_list, index=False)

    def draft_blogs(self):
        query = """select * from draft_blogs"""
        header_list = ['Id', 'Name', 'Published_date', 'blog_Text', 'created_date']
        self.cur.execute(query)
        for record in self.cur.fetchall():
            with open(self.path + record[1] + "-" + record[4].strftime('%b') + "-" + "Draft-blogs.csv", 'a') as f:
                writer = csv.writer(f)
                writer.writerow(record)
            df = pd.read_csv(self.path + record[1] + "-" + record[4].strftime(
                "%b") + "-" + "Draft-blogs.csv", sep=",")
            df.drop_duplicates(subset=None, inplace=True)
            df.to_csv(self.path + record[1] + "-" + record[4].strftime(
                "%b") + "-" + "Draft-blogs.csv", header=header_list, index=False)

    def close(self):
        self.cur.close()
        self.conn.close()


if __name__ == "__main__":
    db = CmsBlogs('localhost', 5432, 'cms', 'josephnaveenkiran', "/Users/josephnaveenkiran/documents/")
    db.published_blogs()
    db.draft_blogs()
    db.close()
