# -*- coding: utf-8 -*-
import re


class CleanHTML:

    def __init__(self):
        pass

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

        total = n1.search(text)
        on_loan = n2.search(text)

        if not (total is None and on_loan is None):
            total = total.group()
            on_loan = on_loan.group()
            total = total.replace('(', '').replace(' ', '').replace('/', '')
            on_loan = on_loan.replace(')', '').replace(' ', '').replace('/', '')
            return {"total": int(total), "on_load": int(on_loan)}
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
    def clean_number(text):
        reg = re.compile(r'(set_number=)[0-9]*')
        total = reg.search(text)

        if total is not None:
            total = total.group()
            return total.replace("set_number=", "")
        else:
            return None

    @staticmethod
    def clean_entry(text):
        reg = re.compile(r'(set_entry=)[0-9]*')
        total = reg.search(text)

        if total is not None:
            total = total.group()
            return total.replace("set_entry=", "")
        else:
            return None
