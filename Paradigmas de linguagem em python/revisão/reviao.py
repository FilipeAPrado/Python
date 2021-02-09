class ConversaoDeUnidadeEmArea:
    @staticmethod
    def ConvertMetroParaPes(num):
        result = int(num) * 10.76
        return result
    
    @staticmethod
    def ConvertPesParaCm(num):
        result = int(num) * 30.48
        return result
    
    @staticmethod
    def ConvertMilhaParaAcre(num):
        result = int(num) * 640
        return result
    
    @staticmethod
    def ConvertAcreParaPes(num):
        result = int(num) * 43560
        return result


print(ConversaoDeUnidadeEmArea.ConvertMetroParaPes(1))