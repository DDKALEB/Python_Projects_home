#!/usr/bin/env python
# coding: utf-8

# HERANÇA

# In[1]:


#EXEMPLO
#VEICULO
##CARRO, CAMIHÃO, MOTO
###CARCTERISTICAS
####CARRO, CAMINHÃO, MOTO


# In[38]:


class ContaBase:
    def __init__(self, numero_conta, titular, saldo):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo

    def extrato(self):
        print("EXTRATO DA CONTA DE", self.titular)
        print("Número da Conta:", self.numero_conta)
        print("Saldo:", self.saldo)

    def saca(self, valor):
        novo_saldo = self.saldo - valor
        if novo_saldo < 0:
            print("Saldo de {} insuficiente para sacar {}".format(self.saldo, valor))
        else:
            self.saldo = novo_saldo

    def deposita(self, valor):
        self.saldo += valor


# Corrigindo a inicialização da classe
conta1 = ContaBase('1', 'Maria', 100)


# In[39]:


class ContaBase():
    #Criar as caracyeristicas da conta...    
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        
    #função dentro de classe = metodos
    def deposita(self, valor):
        self.saldo += valor
    
    def saca(self, valor):
        novo_saldo = self.saldo - valor
        if novo_saldo < 0:
            print("Saldo de {} insuficiente para sacar {}".format(self.saldo,self.valor))
        else:
            self.saldo = novo_saldo
    
    def extrato(self):
        """"Imprime extrato do Titular"""
        print("EXTRATO DA CONTA DE {} \n\tnumero Conta: {} \n\tsaldo: {}".format(self.titular, self.numero, self.saldo))    


# In[40]:


conta1 = ContaBase('1', 'Maria', 100)


# In[41]:


class ContaBase:
    def __init__(self, nome, saldo_inicial):
        self.nome = nome
        self.saldo = saldo_inicial

    def extrato(self):
        print("EXTRATO DA CONTA DE", self.nome)
        print("Número da Conta:", self.numero_conta)
        print("Saldo:", self.saldo)

    def saca(self, valor):
        novo_saldo = self.saldo - valor
        if novo_saldo < 0:
            print("Saldo de {} insuficiente para sacar {}".format(self.saldo, valor))
        else:
            self.saldo = novo_saldo


class Conta(ContaBase):
    def __init__(self, nome, saldo_inicial):
        super().__init__(nome, saldo_inicial)
        self.numero_conta = 1  # Número da conta para Maria


# Testando o código
conta1 = Conta("Maria", 100)
conta1.extrato()
conta1.saca(50)
conta1.extrato()
conta1.saca(60)
conta1.extrato()


# In[42]:


class ContaBase:
    def __init__(self, numero_conta, titular, saldo):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo

    def extrato(self):
        print("EXTRATO DA CONTA DE", self.titular)
        print("Número da Conta:", self.numero_conta)
        print("Saldo:", self.saldo)

    def saca(self, valor):
        novo_saldo = self.saldo - valor
        if novo_saldo < 0:
            print("Saldo de {} insuficiente para sacar {}".format(self.saldo, valor))
        else:
            self.saldo = novo_saldo

    def deposita(self, valor):
        self.saldo += valor


# Corrigindo a inicialização da classe
conta1 = ContaBase('1', 'Maria', 100)


# POUPANÇA

# In[43]:


class ContaPoupanca(ContaBase):
    #Criar as caracyeristicas da conta...    
    def __init__(self, numero, titular, saldo, rendimento=0.01):
        super().__init__(numero, titular, saldo)
        self.rendimento = rendimento
          
    #função dentro de classe = metodos
    def render(self):
        self.saldo += self.saldo * self.rendimento


# In[44]:


class ContaBase:
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def extrato(self):
        print("EXTRATO DA CONTA DE", self.titular)
        print("Número da Conta:", self.numero)
        print("Saldo:", self.saldo)

    def saca(self, valor):
        novo_saldo = self.saldo - valor
        if novo_saldo < 0:
            print("Saldo de {} insuficiente para sacar {}".format(self.saldo, valor))
        else:
            self.saldo = novo_saldo


class ContaPoupanca(ContaBase):
    def __init__(self, numero, titular, saldo, rendimento=0.01):
        super().__init__(numero, titular, saldo)
        self.rendimento = rendimento


# Testando o código
conta_poup = ContaPoupanca('2', 'Maria', 100)
conta_poup.extrato()


# In[45]:


class ContaBase:
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def extrato(self):
        print("EXTRATO DA CONTA DE", self.titular)
        print("Número da Conta:", self.numero)
        print("Saldo:", self.saldo)

    def saca(self, valor):
        novo_saldo = self.saldo - valor
        if novo_saldo < 0:
            print("Saldo de {} insuficiente para sacar {}".format(self.saldo, valor))
        else:
            self.saldo = novo_saldo

    def deposita(self, valor):
        self.saldo += valor


class ContaPoupanca(ContaBase):
    def __init__(self, numero, titular, saldo):
        super().__init__(numero, titular, saldo)
        self.rendimento = 0.01

    def render(self):
        rendimento = self.saldo * self.rendimento
        self.deposita(rendimento)

# Testando o código corrigido
conta_poup = ContaPoupanca('2', 'Maria', 100)
conta_poup.extrato()
conta_poup.render()
conta_poup.extrato()
conta_poup.deposita(150)


# SALARIO

# In[46]:


class ContaSalario(ContaBase):
    #Criar as caracyeristicas da conta...    
    def __init__(self, numero, titular, saldo, salario):
        super().__init__(numero, titular, saldo)
        self.salario = salario
        
    def receber(self):
        self.deposita(seld.salario)
          
    def novo_salario(self, novo_salario):
        self.salario = novo_salario


# In[47]:


conta_sal = ContaSalario('3', 'Maria', 100, 1500)


# In[48]:


class ContaBase:
    def __init__(self, numero_conta, titular, saldo):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo

    def extrato(self):
        print("EXTRATO DA CONTA DE", self.titular)
        print("Número da Conta:", self.numero_conta)
        print("Saldo:", self.saldo)

    def saca(self, valor):
        novo_saldo = self.saldo - valor
        if novo_saldo < 0:
            print("Saldo de {} insuficiente para sacar {}".format(self.saldo, valor))
        else:
            self.saldo = novo_saldo

    def deposita(self, valor):
        self.saldo += valor


class ContaSalario(ContaBase):
    def __init__(self, numero_conta, titular, saldo):
        super().__init__(numero_conta, titular, saldo)
        self.salario = saldo

    def novo_salario(self, salario):
        self.salario = salario

    def receber(self):
        self.deposita(self.salario)


# Testando o código corrigido
conta_sal = ContaSalario(3, 'Maria', 100)
conta_sal.extrato()
conta_sal.saca(1500)
conta_sal.novo_salario(2000)
conta_sal.receber()
conta_sal.extrato()


# CONTA CORRENTE

# In[49]:


class ContaSalario(ContaBase):
    #Criar as caracyeristicas da conta...    
    def __init__(self, numero, titular, saldo, salario):
        super().__init__(numero, titular, saldo)
        self.salario = salario
        
    def receber(self):
        self.deposita(seld.salario)
          
    def novo_salario(self, novo_salario):
        self.salario = novo_salario


# In[ ]:




