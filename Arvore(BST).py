class No:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz_esq = None
        self.raiz_dir = None

class Arvore_Binaria:
    def __init__(self):
        self.raiz = None

    def adicionar(self, num):
        if self.raiz is None:
            self.raiz = No(num)
        else:
            self.adicionar_02(num, self.raiz)

    def adicionar_02(self, num, ra):
        if num < ra.raiz:
            if ra.raiz_esq is not None:
                self.adicionar_02(num, ra.raiz_esq)
            else:
                ra.raiz_esq = No(num)
        else:
            if ra.raiz_dir is not None:
                self.adicionar_02(num, ra.raiz_dir)
            else:
                ra.raiz_dir = No(num)

    def deletar(self, ra, num):
        if not ra: 
            return ra
        if ra.raiz > num: 
            ra.raiz_esq = self.deletar(ra.raiz_esq , num) 
        elif ra.raiz < num: 
            ra.raiz_dir = self.deletar(ra.raiz_dir, num)
        else: 
            if not ra.raiz_dir:
                return ra.raiz_esq
            if not ra.raiz_esq:
                return ra.raiz_dir
            ponte = ra.raiz_dir
            while ponte.raiz_esq:
                ponte = ponte.raiz_esq
            ra.raiz_dir = self.deletar(ra.raiz_dir, ra.raiz)
        return ra

    def busca(self, num):
        if self.raiz is not None:
            return self.busca02(num, self.raiz)
        else:
            print('Vazio')

    def busca02(self, num, ra):
        if num == ra.raiz:
            print('True')
        elif (num < ra.raiz and ra.raiz_esq is not None):
            self.busca02(num, ra.raiz_esq)
        elif (num > ra.raiz and ra.raiz_dir is not None):
            self.busca02(num, ra.raiz_dir)
        else:
            print('False')

    def ord(self, orde, ra):
        if ra.raiz_esq is not None:
            self.ord(orde, ra.raiz_esq)
        if ra.raiz is not None:
            orde.append(ra.raiz)
        if ra.raiz_dir is not None:
            self.ord(orde, ra.raiz_dir)
        return orde
    
    def pre_ord(self, orde, ra):
        if ra.raiz is not None:
            orde.append(ra.raiz)
        if ra.raiz_esq is not None:
            self.pre_ord(orde, ra.raiz_esq)
        if ra.raiz_dir is not None:
            self.pre_ord(orde, ra.raiz_dir)
        return orde
    
    def pos_ord(self, orde, ra):
        if ra.raiz_esq is not None:
            self.pos_ord(orde, ra.raiz_esq)
        if ra.raiz_dir is not None:
            self.pos_ord(orde, ra.raiz_dir)
        if ra.raiz is not None:
            orde.append(ra.raiz)
        return orde

    def altura_arvore(self, ra):
        if ra is None:
            return 0
    
        else :
            esquerda = self.altura_arvore(ra.raiz_esq)
            direita = self.altura_arvore(ra.raiz_dir)
            if (esquerda > direita):
                return esquerda+1
            else:
                return direita+1
    
    def igualdade(self, ra_1, ra_2) :
        if(ra_1 == None and ra_2 == None):
            return True
        elif (ra_1 != None and ra_2 == None) or (ra_1 == None and ra_2 != None) :
            return False
        else:
            if (ra_1.raiz == ra_2.raiz and self.igualdade(ra_1.raiz_esq, ra_2.raiz_esq) and self.igualdade(ra_1.raiz_dir, ra_2.raiz_dir)):
                return True
            else:
                return False

    def teste_balanceado(self, ra, balanceado=True):
        esquerda = self.altura_arvore(ra.raiz_esq)
        direita = self.altura_arvore(ra.raiz_dir)
        if abs(esquerda - direita) > 1:
            balanceado = False
        return balanceado

    def deletar_arvore(self):
        del self.raiz

    def Display(self):
        linhas, *_ = self.Aux_Display(self.raiz)
        for linha in linhas:
            print(linha)

    def Aux_Display(self, ra):
        if ra.raiz_dir is None and ra.raiz_esq is None:
            linha = '%s' % ra.raiz
            largura = len(linha)
            altura = 1
            meio = largura // 2
            return [linha], largura, altura, meio
        if ra.raiz_dir is None:
            linhas, n, p, x = self.Aux_Display(ra.raiz_esq)
            s = '%s' % ra.raiz
            u = len(s)
            Primeira_linha = (x + 1) * ' ' + (n - x - 1) * '_' + s
            Segunda_linha = x * ' ' + '/' + (n - x - 1 + u) * ' '
            linhas_deslocadass = [linha + u * ' ' for linha in linhas]
            return [Primeira_linha, Segunda_linha] + linhas_deslocadass, n + u, p + 2, n + u // 2
        if ra.raiz_esq is None:
            linhas, n, p, x = self.Aux_Display(ra.raiz_dir)
            s = '%s' % ra.raiz
            u = len(s)
            Primeira_linha = s + x * '_' + (n - x) * ' '
            Segunda_linha = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            linhas_deslocadass = [u * ' ' + linha for linha in linhas]
            return [Primeira_linha, Segunda_linha] + linhas_deslocadass, n + u, p + 2, u // 2
        esquerda, n, p, x = self.Aux_Display(ra.raiz_esq)
        direita, m, q, y = self.Aux_Display(ra.raiz_dir)
        s = '%s' % ra.raiz
        u = len(s)
        Primeira_linha = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        Segunda_linha = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            esquerda += [n * ' '] * (q - p)
        elif q < p:
            direita += [m * ' '] * (p - q)
        Linhas_Zipadas = zip(esquerda, direita)
        linhas = [Primeira_linha, Segunda_linha] + [a + u * ' ' + b for a, b in Linhas_Zipadas]
        return linhas, n + m + u, max(p, q) + 2, n + u // 2


ord = [25, 10, 8, 3, 1, 15, 75, 17, 30, 28, 27, 52, 70, 65, 73]
arvore = Arvore_Binaria()
for i in ord:
    arvore.adicionar(i)
arvore.deletar(arvore.raiz, 28)
arvore.deletar(arvore.raiz, 15)
arvore.deletar(arvore.raiz, 75)
arvore.deletar(arvore.raiz, 1)
print()
print('pre-ordem:', arvore.pre_ord([], arvore.raiz))
print()
print('pos-ordem:', arvore.pos_ord([], arvore.raiz))
print()