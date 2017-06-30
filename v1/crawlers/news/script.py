# coding=utf-8
from bs4 import BeautifulSoup

KEY_LIBRARY = {
    "Todas": "Todas las Bibliotecas",
    "BC": "Biblioteca Central.",
    "UCSY": "Centro Peninsular en Humanidades y Ciencias Sociales. mérida, Yucatán.",
    "ISC": "Centro Regional de Investigaciones Multidisciplinarias.",
    "DF3": "Centro Universitario de Estudios Cinematográficos.",
    "CUT": "Centro Universitario de Teatro.",
    "CK": "Centro de Ciencias Aplicadas y Desarrollo Tecnológico.",
    "CFN": "Centro de Ciencias Genómicas.",
    "GM1": "Centro de Ciencias Matemáticas.",
    "CAT": "Centro de Ciencias de la Atmósfera.",
    "CL": "Centro de Enseñanza de Lenguas Extranjeras.",
    "N": "Centro de Enseñanza para Extranjeros.",
    "NT": "Centro de Enseñanza para Extranjeros. Campus Taxco",
    "NSA": "Centro de Enseñanza para Extranjeros. Escuela Permanente de Extensión, San Antonio, Texas, USA",
    "GF3": "Centro de Física Aplicada y Tecnología Avanzada.",
    "I3": "Centro de Geociencias.",
    "CDA": "Centro de Información de Arte, Diseño y Arquitectura.",
    "IIH": "Centro de Investigaciones Interdisciplinarias en Ciencias y Humanidades.",
    "IHM": "Centro de Investigaciones Multidisciplinarias sobre Chiapas y la Frontera Sur. SanCristóbal de las Casas, Chis..",
    "CIEC": "Centro de Investigaciones en Ecosistemas.",
    "GG1": "Centro de Investigaciones en Geografía Ambiental.",
    "CEL": "Centro de Investigaciones sobre América Latina y el Caribe.",
    "EUA": "Centro de Investigaciones sobre América del Norte.",
    "GI2": "Centro de Investigación en Energía.",
    "GF2": "Centro de Nanociencias y Nanotecnología, Ensenada, Baja California.",
    "CGP": "Coordinación de Estudios de Posgrado.",
    "CSAM": "Coordinación de Servicios Administrativos, Morelos.",
    "UA": "Coordinación de Universidad Abierta y Educación a Distancia.",
    "UA1": "Coordinación de Universidad Abierta y Educación a Distancia. Centro de AltaTecnología de "
          "Educación a Distancia",
    "FU": "Dirección General de Actividades Cinematográficas.",
    "CIM": "Dirección General de Artes Visuales.",
    "PUC3": "Dirección General de Cómputo y de Tecnologías de Información y Comunicación. Centro de "
           "Extensión en Cómputo y Telecomunión",
    "PUC": "Dirección General de Cómputo y de Tecnologías de Información y Comunicación.",
    "PUC1": "Dirección General de Cómputo y de Tecnologías de Información y Comunicación. Centro de "
           "Extensión en Cómputo y Telecomunión",
    "PUC2": "Dirección General de Cómputo y de Tecnologías de Información y Comunicación. Centrode "
           "Extensión en Cómputo y Telecomunión",
    "DD": "Dirección General de Deporte Universitario.",
    "PCC": "Dirección General de Divulgación de la Ciencia.",
    "LU": "Dirección General de Estudios de Legislación Universitaria.",
    "DM": "Dirección General de Servicios médicos.", "DTU": "Dirección General de Televisión Universitaria.",
    "CCH": "Dirección General de la Escuela Nacional del Colegio de Ciencias y Humanidades.",
    "L": "Dirección General de la Escuela NacionalPreparatoria.",
    "CYHB": "Escuela Nacional Colegio de Ciencias y Humanidades, Plantel Azcapotzalco.",
    "CYHA": "Escuela Nacional Colegio de Ciencias y Humanidades, Plantel Naucalpan.",
    "CYHE": "Escuela Nacional Colegio de Ciencias y Humanidades, Plantel Oriente.",
    "CYHD": "Escuela Nacional Colegio de Ciencias y Humanidades, Plantel Sur.",
    "CYHC": "Escuela Nacional Colegio de Ciencias y Humanidades, Plantel Vallejo.",
    "L1": "Escuela Nacional Preparatoria Plantel Uno Gabino Barreda.",
    "L5": "Escuela Nacional Preparatoria. Plantel Cinco José Vasconcelos.",
    "L4": "Escuela Nacional Preparatoria. Plantel Cuatro, Vidal Castañeda y Nájera.",
    "L2": "Escuela Nacional Preparatoria. Plantel Dos Erasmo Castellanos Quinto.",
    "L19": "Escuela Nacional Preparatoria. Plantel Nueve Pedro de Alba.",
    "L18": "Escuela Nacional Preparatoria. Plantel Ocho Miguel E. Schulz.",
    "L6": "Escuela Nacional Preparatoria. Plantel Seis Antonio Caso.",
    "L7": "Escuela Nacional Preparatoria. Plantel Siete Ezequiel A. Chávez.",
    "L3": "Escuela Nacional Preparatoria. Plantel Tres Justo Sierra.",
    "HB": "Escuela Nacional de Enfermería y Obstetricia.",
    "ENESL": "Escuela Nacional de Estudios Superiores Campus León.",
    "ENESM": "Escuela Nacional de Estudios Superiores Campus Morelia.",
    "TS": "Escuela Nacional de Trabajo Social.",
    "BA": "Facultad de Arquitectura.",
    "BAI": "Facultad de Arquitectura. Centro de Investigaciones de Diseño Industrial",
    "CMP1": "Facultad de Arquitectura. División de Estudios de Posgrado",
    "B1": "Facultad de Artes y Diseño. División de Estudios de Posgrado",
    "B": "Facultad de Artes y Diseño.",
    "B2": "Facultad de Artes y Diseño. Taxco.",
    "FC": "Facultad de Ciencias. División de Estudios de Profesionales",
    "CP": "Facultad de Ciencias Políticas y Sociales.",
    "C": "Facultad de Contaduría y Administración.",
    "D": "Facultad de Derecho.",
    "Q": "Facultad de Economía.",
    "ACA": "Facultad de Estudios Superiores Acatlán.",
    "ARA": "Facultad de Estudios Superiores Aragón.",
    "CUA": "Facultad de Estudios Superiores Cuautitlán.",
    "IZT": "Facultad de Estudios Superiores Iztacala.",
    "ZAR3": "Facultad de Estudios Superiores Zaragoza. Campus III",
    "ZAR": "Facultad de Estudios Superiores Zaragoza.",
    "ZAR2": "Facultad de Estudios Superiores Zaragoza. Campo Dos", "F": "Facultad de Filosofía y Letras.",
    "G": "Facultad de Ingeniería.",
    "G1": "Facultad de Ingeniería. División de Estudios Profesionales (Anexo)",
    "GH3": "Facultad de Ingeniería. Acervo Histórico",
    "G3": "Facultad de Ingeniería. División de Educación Continua y a Distancia",
    "G2": "Facultad de Ingeniería. Estudios de Posgrado",
    "HBM1": "Facultad de Medicina. Colección Doctores Ramón y Juan Ramón De la Fuente",
    "H": "Facultad de Medicina.",
    "HF": "Facultad de Medicina. División de Estudios de Posgrado e Investigación",
    "H3": "Facultad de Medicina. Departamento de Psicología médica, Psiquiatría y Salud Mental",
    "H6": "Facultad de Medicina. Departamento de Medicina Familiar",
    "HBM": "Facultad de Medicina. Departamento de Historia y Filosofia de la Medicina",
    "P": "Facultad de Medicina Veterinaria y Zootecnia.",
    "EIB": "Facultad de Medicina Veterinaria y Zootecnia. Centro de Enseñanza, Investigación y Extensión "
          "en Producción Ovina",
    "RCM": "Facultad de Medicina Veterinaria y Zootecnia. Centro de Enseñanza, Investigación y Extensión "
          "en Producción Animal en Alta",
    "GEP": "Facultad de Medicina Veterinaria y Zootecnia. Centro de Enseñanza, Investigación y Extensión "
          "en Producción Porcina",
    "GEA": "Facultad de Medicina Veterinaria y Zootecnia. Centro de Enseñanza, Investigación y Extensión "
          "en Producción Avícola",
    "J": "Facultad de Música.",
    "K": "Facultad de Odontología. División de Estudios Profesionales",
    "K1": "Facultad de Odontología. División de Estudios de Posgrado",
    "PS": "Facultad de Psicología. División de Estudios Profesionales",
    "PS1": "Facultad de Psicología. División de Estudios de Posgrado",
    "M": "Facultad de Química.",
    "M2": "Facultad de Química. División de Estudios Profesionales Anexo",
    "M1": "Facultad de Química. División de Estudios de Posgrado",
    "M3": "Facultad de Química. División de Estudios de Posgrado Anexo",
    "B4": "Fondo Bibliográfico. Antigua Academia de San Carlos.",
    "A": "Instituto de Astronomía.",
    "A1": "Instituto de Astronomía. Observatorio Astronómico Nacional San Pedro Mártir, Baja California",
    "A2": "Instituto de Astronomía. Centro de Radioastronomía y Astrofísica. Campus Morelia",
    "E": "Instituto de Biología.",
    "E1": "Instituto de Biología. Estación Biológica Tropical - Los Tuxtlas, Veracruz",
    "E2": "Instituto de Biología. Estación de Investigación Experimentación y Difusión - Chamela, Jalisco",
    "CGB": "Instituto de Biotecnología.",
    "GF1": "Instituto de Ciencias Físicas, Cuernavaca.",
    "NC": "Instituto de Ciencias Nucleares.",
    "MAR": "Instituto de Ciencias del Mar y Limnología.",
    "MAR1": "Instituto de Ciencias del Mar y Limnología. Estación Ciudad del Carmen, Campeche",
    "MAR2": "Instituto de Ciencias del Mar y Limnología. Unidad Académica Mazatlán",
    "MAR3": "Instituto de Ciencias del Mar y Limnología. Unidad Académica de Puerto Morelos, Quintana Roo",
    "CCE": "Instituto de Ecología.",
    "CFC": "Instituto de Fisiología Celular.",
    "GF": "Instituto de Física.",
    "IF": "Instituto de Geofísica.",
    "GG": "Instituto de Geografía.",
    "I": "Instituto de Geología.",
    "II": "Instituto de Ingeniería.",
    "AN": "Instituto de Investigaciones Antropológicas.",
    "CIB": "Instituto de Investigaciones Bibliotecológicas y de la Información.",
    "HE": "Instituto de Investigaciones Biomédicas.",
    "IQ": "Instituto de Investigaciones Económicas.",
    "BE": "Instituto de Investigaciones Estéticas.",
    "FL": "Instituto de Investigaciones Filológicas.",
    "FE": "Instituto de Investigaciones Filosóficas.",
    "FH": "Instituto de Investigaciones Históricas.",
    "DC": "Instituto de Investigaciones Jurídicas.",
    "DS": "Instituto de Investigaciones Sociales.",
    "CE": "Instituto de Investigaciones en Matemáticas Aplicadas y en Sistemas.",
    "GI": "Instituto de Investigaciones en Materiales.",
    "CEU": "Instituto de Investigaciones sobre la Universidad y la Educación.",
    "GM": "Instituto de Matemáticas.",
    "GM2": "Instituto de Matemáticas. Unidad Cuernavaca, Morelos",
    "CNQ": "Instituto de Neurobiología.",
    "MQ": "Instituto de Química.",
    "MUCON": "Museo de las Constituciones.",
    "PUDH": "Programa Universitario de Derechos Humanos.",
    "PUED": "Programa Universitario de Estudios de Desarrollo.",
    "PEG": "Programa Universitario de Estudios de Género.",
    "PEC": "Programa Universitario de Estudios sobre la Ciudad.",
    "CCTL": "Proyecto Juan Acha Centro Cultural Universitario Tlatelolco.",
    "UAER": "Unidad Académica de Estudios Regionales, la Ciénega, Jiquilpan, Michoacán.",
    "UDIRM": "Unidad de Investigación sobre Representaciones Culturales y Sociales, CampusMorelia."
}
ecj_data = open("/home/regoeco/Documentos/projects/books-unam/bapi/v1/crawlers/news/schools.html",'r').read()
soup_result = BeautifulSoup(ecj_data, "html.parser", from_encoding = 'utf-8')
options = soup_result.find_all('option')
for o in options:
    print 'a[\"' + o['value'] + '\"]' + " = " + '\"' + o.text + '\"'
