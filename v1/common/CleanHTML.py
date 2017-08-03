# -*- coding: utf-8 -*-
import re


class CleanHTML:

    def __init__(self):
        pass

    @staticmethod
    def get_google_book_id(text):
        reg = re.compile(r"(id=)(.*?)(\\)")
        r = reg.search(text)

        if r is not None:
            r = r.group()
            return r.replace("id=", "").replace("\\", "")
        else:
            return None

    @staticmethod
    def get_title(text):
        reg = re.compile(r"(title = ')(.*?)(\/)")
        r = reg.search(text)

        if r is not None:
            r = r.group()
            return r.replace("title = '", "").replace("/", "")
        else:
            return None

    @staticmethod
    def clean_session(text):
        """
        RETURN SESSION EXAMPLE 
        http://biblioteca-fes.aragon.unam.mx:8991/F/9L3VS19J11CIMATJ1DHCVXIXAGQF4F3PSXV5NFLE4LCHXPVI9P-03069?func=logout
        :param text: 
        :return: 
        """
        patron = re.compile(r'(F/)(.*)(\?)')
        s = patron.search(text)
        if s is not None:
            session = s.group()
            session = session.replace('F/', '').replace('?', '')
            return session
        else:
            return None

    @staticmethod
    def clean_block(text):
        patron = re.compile(r'[0-9]*$')
        s = patron.search(text)
        block = None
        if s is not None:
            block = s.group()
        return block

    @staticmethod
    def clean_copies(text):
        n1 = re.compile(r'(\()(.*)(/)')
        n2 = re.compile(r'(/)(.*)(\))')

        copies = n1.search(text)
        on_loan = n2.search(text)

        if not (copies is None and on_loan is None):
            copies = copies.group()
            on_loan = on_loan.group()
            copies = copies.replace('(', '').replace(' ', '').replace('/', '')
            on_loan = on_loan.replace(')', '').replace(' ', '').replace('/', '')
            return {"copies": int(copies), "on_loan": int(on_loan)}
        else:
            return None

    @staticmethod
    def clean_total(text):
        reg = re.compile(r'[0-9]*$')
        total = reg.search(text)

        if total is not None:
            return total.group()
        else:
            return None
    
    @staticmethod
    def clean_blank_space(text):
        reg = re.compile(r'( )*$')
        t = reg.sub("", text)
        return t

    @staticmethod
    def get_set_number(text):
        """
        text = 
            http://biblioteca-fes.aragon.unam.mx:8991/F/SX25U2QYGN94EA582TRXG636DCQTG7MCDYIABS2U66XGY9DFGL-05202?
            func=full-set-set&set_number=000131&set_entry=000001&format=999
        :param text: 
        :return: 
        """
        reg = re.compile(r'(set_number=)[0-9]*')
        r = reg.search(text)

        if r is not None:
            r = r.group()
            return r.replace("set_number=", "")
        else:
            return None

    @staticmethod
    def get_set_entry(text):
        """
        text = 
            http://biblioteca-fes.aragon.unam.mx:8991/F/SX25U2QYGN94EA582TRXG636DCQTG7MCDYIABS2U66XGY9DFGL-05202?
            func=full-set-set&set_number=000131&set_entry=000001&format=999
        :param text: 
        :return: 
        """
        reg = re.compile(r'(set_entry=)[0-9]*')
        r = reg.search(text)

        if r is not None:
            r = r.group()
            return r.replace("set_entry=", "")
        else:
            return None

    @staticmethod
    def get_jump(text):
        """
        text = 
            http://biblioteca-fes.aragon.unam.mx:8991/F/DCQ2GBRBAYBK91IAGKGAEGAP298MVEJEC23FRNNPFQ88US6DHT-06135?
            func=short-jump&jump=000011
        :param text: 
        :return: 
        """
        reg = re.compile(r'(jump=)[0-9]*')
        r = reg.search(text)

        if r is not None:
            r = r.group()
            return r.replace("jump=", "")
        else:
            return None

    @staticmethod
    def get_doc_library(text):
        """
               text = 
                   http://biblioteca-fes.aragon.unam.mx:8991/F/DCQ2GBRBAYBK91IAGKGAEGAP298MVEJEC23FRNNPFQ88US6DHT-06135?
                   func=item-global&doc_library=L0801&doc_number=001918315&year=&volume=&sub_library=L08
               :param text: 
               :return: 
               """
        reg = re.compile(r'(doc_library=)(.*?)(&)')
        r = reg.search(text)

        if r is not None:
            r = r.group()
            return r.replace("doc_library=", "").replace("&", "")
        else:
            return None

    @staticmethod
    def get_doc_number(text):
        """
        text = 
            http://biblioteca-fes.aragon.unam.mx:8991/F/DCQ2GBRBAYBK91IAGKGAEGAP298MVEJEC23FRNNPFQ88US6DHT-06135?
            func=item-global&doc_library=L0801&doc_number=001918315&year=&volume=&sub_library=L08
        :param text: 
        :return: 
        """
        reg = re.compile(r'(doc_number=)[0-9]*')
        r = reg.search(text)

        if r is not None:
            r = r.group()
            return r.replace("doc_number=", "")
        else:
            return None

    @staticmethod
    def get_sub_library(text):
        """
               text = 
                   http://biblioteca-fes.aragon.unam.mx:8991/F/DCQ2GBRBAYBK91IAGKGAEGAP298MVEJEC23FRNNPFQ88US6DHT-06135?
                   func=item-global&doc_library=L0801&doc_number=001918315&year=&volume=&sub_library=L08
               :param text: 
               :return: 
               """
        reg = re.compile(r'(sub_library=)(.*)')
        r = reg.search(text)

        if r is not None:
            r = r.group()
            return r.replace("sub_library=", "")
        else:
            return None

    @staticmethod
    def get_link_img_google(text):
        reg = re.compile(r'("thumbnail_url":")(.*?)(")')
        r = reg.search(text)

        if r is not None:
            r = r.group()
            return r.replace("\"thumbnail_url\":\"", "").replace("\"", "").replace("\u0026", "&")
        else:
            return None

    def get_link_info_url(text):
        reg = re.compile(r'("info_url":")(.*?)(")')
        r = reg.search(text)

        if r is not None:
            r = r.group()
            return r.replace("\"info_url\":\"", "").replace("\"", "").replace("\u0026", "&")
        else:
            return None


    def get_link_preview_url(text):
        reg = re.compile(r'("preview_url":")(.*?)(")')
        r = reg.search(text)

        if r is not None:
            r = r.group()
            return r.replace("\"preview_url\":\"", "").replace("\"", "").replace("\u0026", "&")
        else:
            return None

    @staticmethod
    def clean_total_registros(text):
        return int(text.replace("Total de registros:", ""))

# 12/12/2015