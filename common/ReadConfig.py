import yaml
import os
os.path.join("..")


class YamlReader:
    def __init__(self, yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError('文件不存在！')
        self._data = None

    @property
    def data(self):
        # 如果是第一次调用data，读取yaml文档，否则直接返回之前保存的数据
        if not self._data:
            with open(self.yamlf, 'rb') as f:
                self._data = list(yaml.safe_load_all(f))  # load后是个generator，用list组织成列表
        return self._data
class Config:
    def __init__(self, config):
        self.config = YamlReader(config).data

    def get(self, date = None,index=0):
        self.config[index].update()
        return self.config[index].get(date)


if __name__ == '__main__':
    from BasePath import path
    a = path.MysqlConfig
    c = Config(a).get("testdb")["host"]
    print(c)

