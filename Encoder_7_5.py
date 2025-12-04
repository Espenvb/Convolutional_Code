class Conv_7_5_enc:
    def __init__(self):
        self.state = 0b00

    def encode_bit(self, bit):
        code = 0b00
        match self.state:
            case 0b00:
                if(bit == 0b1):
                    self.state = 0b10
                    code = 0b11
                else:
                    code = 0b00
            case 0b10:
                if(bit == 0b1):
                    self.state = 0b11
                    code = 0b10
                else:
                    self.state = 0b01
                    code = 0b01
            case 0b01:
                if(bit == 0b1):
                    self.state = 0b10
                    code = 0b00
                else:
                    self.state = 0b00
                    code = 0b11
            case 0b11:
                if(bit == 0b1):
                    code = 0b01
                else:
                    self.state = 0b01
                    code = 0b10
        
        return code
    
    def encode_symbol(self, symbol, length):
        code = []
        for i in range(length):   # 7 → 0
            bit = symbol[i]
            code.append(self.encode_bit(bit))
        code.append(self.encode_bit(0))
        code.append(self.encode_bit(0))
        return code

        
        
            
