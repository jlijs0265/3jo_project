import pandas as pd

class Recommend:
    #생성자
    # data : 초기 데이터
    def __init__(self, webtoon_name, webtoon_genre):
        self.data = pd.read_csv('output.csv')
        self.input_name = webtoon_name[0]
        self.input_genre = webtoon_genre[0]

    # 입력값이 1개일때 가정.
    # 입력값이 여러개라면..

    # 일치하는 군집 찾기
    def find_cluster(self): 
        if (type(self.input_name)==str) & (self.input_genre == '무관'):
            cluster_num = self.data.loc[self.data['name']==self.input_name][['label','category']].values[0]
            return  cluster_num
        else :
            return '오류 발생'
    # 이미지 군집, 자연어 군집
    # 이미지, 자연어 같은 군집인것 찾기
    def select(self, image, nlp):
        # webtoon_name_df = self.data.loc[(self.data['label']==image)&(self.data['category']==nlp)].loc[~(self.data['name'] == self.input_name)]
        # webtoon_name = webtoon_name_df.sort_values('order', ascending= False)['name'].values[0:5]
        # if webtoon_name.size == 0 :
        webtoon_name_df = self.data.loc[(self.data['label']==image)|(self.data['category']==nlp)].loc[~(self.data['name'] == self.input_name)]
        webtoon_name = webtoon_name_df.sort_values('order', ascending= False)['name'].values[0:6]
        return webtoon_name

    # 소개글
    def find_summary(self, webtoon_name):
        summary = self.data['summary'].loc[self.data['name']==webtoon_name]
        return summary
    
    # 썸네일
    def find_thumb(self, webtoon_name):
        thumb = self.data['tumb'].loc[self.data['name']==webtoon_name]
        return thumb

    # 주소
    def find_link(self, webtoon_name):
        link = self.data['link'].loc[self.data['name']==webtoon_name].values[0]
        return link