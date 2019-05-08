from lxml import html
import requests
import csv

studiesObject = []
# studiesStringArray = []

# for letter in range(65, 91):
#     # print("--------------------------Init letter: "+chr(letter));

#     url = 'https://www.universidadesmex.com/listado_carreras.php?l=' + \
#         chr(letter)

#     page = requests.get(url)
#     tree = html.fromstring(page.content)

#     temp = tree.xpath('//ul[@class="list-regular"]/li/a/p/text()')

#     for study in temp:
#         studiesStringArray.append(study)


studiesStringArray = ['Abordaje de Problemas Críticos de la Pareja', 'Actuación', 'Actuaría', 'Acuarela', 'Administración', 'Administración de Capital Humano', 'Administración de Empresas', 'Administración de Empresas de Hospitalidad', 'Administración de Empresas de Hospitalidad, Gastronómicas y Turísticas', 'Administración de Empresas Sustentables', 'Administración de Empresas Turísticas', 'Administración de Finanzas', 'Administración de Hospitales', 'Administración de Hospitales y Salud Pública', 'Administración de Instituciones Educativas', 'Administración de la Capacitación del Capital Humano', 'Administración de la Construcción', 'Administración de la Hospitalidad', 'Administración de la Tecnología Educativa', 'Administración de la Tesorería', 'Administración de Negocios', 'Administración de Negocios de Comunicación y Entretenimiento', 'Administración de Negocios en Calidad y Productividad', 'Administración de Negocios en Finanzas', 'Administración de Negocios en Mercadotecnia', 'Administración de Negocios en Recursos Humanos', 'Administración de Negocios Internacionales', 'Administración de Organizaciones', 'Administración de Proyectos', 'Administración de Recursos Humanos', 'Administración de Recursos Telemáticos', 'Administración de Restaurantes', 'Administración de Riesgos', 'Administración de Servicios de Tecnología de la Información', 'Administración de Sistemas de Productividad y Calidad', 'Administración de Tecnologías de la Información', 'Administración del Vino', 'Administración Empresarial', 'Administración Estratégica', 'Administración Financiera', 'Administración Global de Negocios', 'Administración Hotelera', 'Administración Hotelera y Turística', 'Administración Industrial', 'Administración Modalidad Mixta', 'Administración Municipal', 'Administración Pública', 'Administración Pública y Gobierno', 'Administración Social de la Salud', 'Administración Turística', 'Administración y Dirección de Empresas', 'Administración y Estrategia de Negocios', 'Administración y Finanzas', 'Administración y Gestión de Organizaciones', 'Administración y Mercadotecnia', 'Administración y Productividad', 'Adobe Director CS', 'Adobe Illustrator CS3', 'Agencia de Viajes', 'Agronomía', 'Alimentación Masiva', 'Alta Dirección', 'Alta Dirección Corporativa', 'Alta Dirección de Empresas Turísticas', 'Ambiental y Sustentabilidad', 'Amparo', 'Análisis y Tecnología de Alimentos', 'Anestesiología', 'Animación y Arte Digital', 'Animación y Efectos Visuales', 'Año Integral', 'Antropología Cultural', 'Antropología Educativa', 'Antropología Filosófica', 'Antropología Religiosa', 'Antropología Social', 'Arquitecto Constructor', 'Arquitectura', 'Arquitectura de Interiores', 'Arquitectura de Interiores y Ambientación', 'Arquitectura Religiosa Virreinal', 'Arte', 'Arte Antiguo', 'Arte del Siglo XX', 'Arte Moderno y Contemporáneo', 'Artes Culinarias', 'Artes Plásticas', 'Atención a la Diversidad e Inclusión Escolar', 'Auditoría y control interno para la detección de fraude', 'Autoconocimiento y Desarrollo Humano', 'Básico de Impuestos', 'Bioética', 'Biomédico', 'Biotecnología', 'Body Paint Artístico y Comercial', 'Calidad de la Atención Clínica', 'Cardiología', 'Cátedra de Cirugía', 'Cerámica', 'Ciencia de Datos', 'Ciencia y Tecnología Alimentaria', 'Ciencias Administrativas', 'Ciencias Aduanales y Comercio Exterior ', 'Ciencias de Ingeniería', 'Ciencias de la Administración', 'Ciencias de la Computación', 'Ciencias de la Comunicación', 'Ciencias de la Comunicación y Periodismo', 'Ciencias de la Educación', 'Ciencias de la Educación', 'Ciencias de la Familia', 'Ciencias de la Familia (en línea)', 'Ciencias de la Familia para la Consultoría', 'Ciencias de la Informática', 'Ciencias de la Ingeniería', 'Ciencias del Deporte', 'Ciencias del Desarrollo Humano', 'Ciencias Econòmicas Administrativas', 'Ciencias en Computación', 'Ciencias en Ingeniería Química', 'Ciencias Financieras', 'Ciencias Juridicas', 'Ciencias Penales', 'Ciencias Penales y Criminalística', 'Ciencias Políticas', 'Ciencias Políticas y Administración Pública', 'Ciencias Sociales', 'Ciencias Sociales y Administrativas', 'Ciencias Sociales y Políticas', 'Ciencias Teológicas', 'Ciencias y Técnicas de la Comunicación', 'Ciencias y Técnicas de la Educación', 'Cine club', 'Cine Méxicano: Sus Figuras y Vertientes', 'Cine y Televisión', 'Cine y TV Digital', 'Cinematografía', 'Cirugía Bucal de Gabinete', 'Cirugía General', 'Cirujano Dentista', 'Clínica Psicoanalítica', 'Coaching', 'Cognición y Lenguaje', 'Comercio Exterior', 'Comercio Internacional', 'Comercio Internacional y Aduanas', 'Comercio y Finanzas Internacionales', 'Comercio y Logística Internacionales', 'Comercio y Negocios Internacionales', 'Cómo Vender Diseño Gráfico', 'Computación', 'Computación Administrativa', 'Computadoras en la Educación', 'Comunicación', 'Comunicación Educativa', 'Comunicación Empresarial', 'Comunicación Estratégica para el mercado Global', 'Comunicación Humana', 'Comunicación Organizacional', 'Comunicación Periodística y sus Nuevas Tecnologías', 'Comunicación Visual', 'Comunicación y Coaching Familiar', 'Comunicación y Medios Digitales', 'Comunicación y Multimedios', 'Comunicación y R.P', 'Construcción', 'Construcción de Carreteras', 'Construcción de Escuelas', 'Construcción de Hospitales', 'Construcción de Proyectos Hidráulicos', 'Consultor de Negocios', 'Consultor PYMES', 'Contabilidad', 'Contabilidad con Especialidad en Impuestos', 'Contador Auditor Privado', 'Contador Público', 'Contador Público con Énfasis en Contraloría Empresarial', 'Contaduría', 'Contaduría Pública', 'Contaduría Pública y Estrategia Financiera', 'Contaduría Pública y Finanzas', 'Contaduría y Finanzas', 'Contaduría y Gestión Empresarial', 'Contaduría y Gestión Financiera', 'Continuidad y Actualización', 'Counseling', 'Creación de Estrategias Integrales 360', 'Creación y Administración de PYMES', 'Creación y Desarrollo de Empresas', 'Creatividad y Estrategias Publicitarias', 'Criminalísta', 'Criminalística y Criminología', 'Criminología', 'Criminología y Criminalística', 'Cultura Prehispánica', 'Curso de Corel Draw', 'Curso de Dibujo Básico', 'De la Estrategia Creativa a la Producción de un Comercial', 'Deportiva', 'Derecho', 'Derecho Administrativo y Fiscal', 'Derecho Civil', 'Derecho Comparado', 'Derecho con acentuación en Economía', 'Derecho Constitucional y Amparo', 'Derecho Corporativo', 'Derecho Corporativo y Negocios Internacionales', 'Derecho de Amparo', 'Derecho Fiscal', 'Derecho General', 'Derecho Laboral', 'Derecho Mercantil', 'Derecho Penal', 'Derecho Penal con Énfasis en Juicios Adversariales', 'Derecho Procesal Administrativo', 'Derecho Público', 'Derecho Tributario', 'Derecho y Ciencia Política', 'Derecho y Ciencias Jurídicas', 'Derecho y Finanzas', 'Derechos Humanos', 'Derechos Humanos y Garantías', 'Desafíos para la Mujer Actual', 'Desarolladores Turísticos', 'Desarrolladores de Vivienda', 'Desarrollo de Negocios y Dirección de Empresas Turísticas', 'Desarrollo de Proyectos de Participación Público-Privadas', 'Desarrollo de Software', 'Desarrollo de Soluciones.NET', 'Desarrollo de Tecnologías de Información', 'Desarrollo Empresarial', 'Desarrollo Humano', 'Desarrollo Organizacional', 'Desarrollo Sustentable', 'Dibujo', 'Diplomado en Alta Dirección', 'Diplomado en Aminación 3D', 'Diplomado en Marketing Deportivo', 'Diplomado en Marketing Digital', 'Diplomado en Mercadotecnia Política', 'Diplomado en Producción Audiovisual', 'Diplomado en Publicidad y Medios', 'Diplomado en Relaciones Públicas (semipresencial)', 'Diplomado Insight del Consumidor', 'Dirección de Arte para Cine y Televisión', 'Dirección de Empresas', 'Dirección de Empresas de Entretenimiento', 'Dirección de Negocios del Entretenimiento', 'Dirección de Organizaciones', 'Dirección de Proyectos', 'Dirección de Restaurantes', 'Dirección en Responsabilidad Social y Desarrollo Sustentable', 'Dirección en Ventas', 'Dirección Financiera', 'Dirección Global de Negocios', 'Dirección Hotelera', 'Dirección Internacional', 'Dirección Internacional de Hoteles', 'Dirección y Administración de Empresas', 'Dirección y Administración de Instituciones de Salud', 'Dirección y Administración del Deporte', 'Disciplina Alexander', 'Diseño', 'Diseño Arquitectónico', 'Diseño Automotriz', 'Diseño de Animación', 'Diseño de Bolsas y Carteras', 'Diseño de Indumentaria y Moda', 'Diseño de Interiores', 'Diseño de Joyería', 'Diseño de la Moda e Industria del Vestido', 'Diseño de la Moda e Industria del Vestido con Certificado NABA', 'Diseño de Moda y Textiles', 'Diseño de Modas', 'Diseño de Patrones Industriales', 'Diseño Digital', 'Diseño en Medios Digitales', 'Diseño Estratégico e Innovación', 'Diseño Gráfico', 'Diseño Gráfico con Certificado NABA', 'Diseño Gráfico y Animación', 'Diseño Industrial', 'Diseño Industrial con Certificado NABA', 'Diseño Interactivo', 'Diseño Multimedia', 'Diseño Multimedia y Arte Digital', 'Diseño para la Comunicación en Medios Digitales', 'Diseño Publicitario', 'Diseño Textil', 'Diseño Textil y Moda', 'Diseño y Animación Digital', 'Diseño y Complementos (Bolsos) Moda', 'Diseño y Comunicación Visual', 'Diseño y Creación de Calzado', 'Docencia', 'Docencia Universitaria', 'Economía', 'Economía y Finanzas', 'Educación', 'Educación Basada en Competencias', 'Educación con Orientación en Dirección y Gestión de Instituciones Educativas', 'Educación con Orientación en Innovación y Tecnologías Educativas', 'Educación con Orientación en Tutoría', 'Educación en Competencias Educativas', 'Educación Familiar', 'Educación Preescolar', 'Educación Primaria', 'Educación Secundaria', 'Educación Superior', 'Educación y Desarrollo', 'Educación y Desarrollo Humano', 'Ejecución de Obra Pública', 'Ejecutiva en Administración', 'Emprendimiento Cultural y Social', 'Endodoncia', 'Endoperio', 'Enfermera Partera', 'Enfermería', 'Enfermería y Obstetricia', 'Enseñanza de la Lengua Inglesa', 'Enseñanza del Hebreo', 'Enseñanza del Idioma Inglés como Segunda Lengua', 'Enseñanza del Inglés', 'Enseñanza del Inglés Modalidad Mixta', 'Enseñanza Superior', 'Envase y Embalaje', 'Escultura', 'Especialidad en impuestos', 'Especialidad Endodoncia', 'Especialidad Odontología Pedíatrica', 'Especialidad Ortodoncia', 'Estética Dental', 'Estomatología', 'Estudios de Arte', 'Estudios de Diseño', 'Estudios Diplomáticos', 'Estudios Humanísticos', 'Estudios Judaicos', 'Evaluación Neuropsicológica en el Adulto', 'Evaluación Psicológica en la Clínica y la Escuela', 'Excel Avanzado', 'Excutive MBA', 'Familia: estructura, conflictos y terapia', 'Fashion Design and Marketing', 'Filosofía', 'Filosofía del Derecho', 'Finanzas', 'Finanzas Corporativas y Bancas', 'Finanzas Empresariales', 'Finanzas en Alta Dirección', 'Finanzas y Banca', 'Finanzas y Contaduría Pública', 'Fiscal', 'Físico Industrial', 'Fisioterapia', 'Fisioterapia Deportiva', 'Flash', 'Formación Integral', 'Fotografía', 'Fotografía Periodística', 'Gastronomía', 'Gastronomía y Administración Operativa',
                      'Gastronomía y Artes Culinarias', 'Gastronomía y Gestión Restaurantera', 'Geotecnia', 'Gerencia de Programas Sanitarios en Inocuidad y Alimentos', 'Gerencia de Proyectos', 'Geriatría', 'Gerontología', 'Gestión Administrativa', 'Gestión de Áreas Protegidas y Desarrollo Ecorregional', 'Gestión de Comercio Electrónico', 'Gestión de la Innovación Tecnológica', 'Gestión de Negocios Gastronómicos', 'Gestión de Negocios Turísticos', 'Gestión de Tecnologías de la Información', 'Gestión Directiva en Salud', 'Gestión e Innovación Educativa', 'Gestión Fiscal de Inversiones', 'Gestión Turística', 'Gestión y Administración de Proyectos', 'Gestión y Finanzas Públicas', 'Ginecología y Obstetricia', 'Gobierno y Política Pública', 'Grafología', 'Guión Cinematográfica', 'Historia', 'Historia de México', 'Historia del Arte', 'Historia y Arte', 'Humanidades', 'Humanismo y Cultura', 'Iconografía del Arte Virreinal Mexicano', 'Idiomas', 'Ilustración de Fantasía y Ficción', 'Impacto y Gestión Ambiental', 'Implantología', 'Impuestos', 'Industrial', 'Industrial y de Sistemas', 'Industrias Alimentarias', 'Informática', 'Informática Administrativa', 'Informática Forense', 'Informática y Tecnologías de Información', 'Ingeniería Ambiental', 'Ingeniería Biomédica', 'Ingeniería Civil', 'Ingeniería Comercial', 'Ingeniería con Especialidad en Administración de la Construcción', 'Ingeniería de la Calidad', 'Ingeniería de Sistemas', 'Ingeniería de Software', 'Ingeniería del Mantenimiento de obra civil', 'Ingeniería en Alimentos', 'Ingeniería en Dirección de Negocios', 'Ingeniería en Diseño y Animación Digital', 'Ingeniería en Energía y Desarrollo Sustentable', 'Ingeniería en Mecatrónica', 'Ingeniería en Negocios y Tecnologías de la Manufactura', 'Ingeniería en Sistemas Computacionales', 'Ingeniería en Sistemas Electrónicos', 'Ingeniería en Tecnología Interactiva en Animación Digital', 'Ingeniería en Tecnologías Computacionales', 'Ingeniería en Telecomunicaciones y Electrónica', 'Ingeniería en Telemática y Sistemas de Seguridad', 'Ingeniería Física', 'Ingeniería Industrial', 'Ingeniería Industrial y de Sistemas', 'Ingeniería Mecánica Industrial', 'Ingeniería Química de la Dirección', 'Ingeniería Telemática', 'Ingeniería y Administración de la Construcción', 'Ingeniero Constructor', 'Innovación Educativa', 'Innovación Industrial', 'Innovación y Desarrollo', 'Innovación y Dirección de Negocios', 'Inteligencia de Negocios', 'Inteligencia Emocional y Desarrollo Integral', 'Interinstitucional en Educación', 'Internacional en Bienestar Social', 'Internado Pregrado', 'Interpretación', 'Interpretación Judicial Constitucional', 'Intérprete Traductor', 'Intervención Emocional en al Educación Especial ', 'Introducción al Cine Documental', 'Investigación de Mercados', 'Investigación de Mercados para la Toma de Decisiones Empresariales', 'Investigación Psicoanalítica ', 'Investigación Psicológica', 'Investigación y Desarrollo de la Educación', 'Investigación y Psicoanálisis', 'ISR sueldos y salarios', 'Juicio de Amparo', 'Justicia Penal y Seguridad Pública', 'Legislación Aduanera', 'Legislación Ambiental', 'Legislación Empresarial', 'Lenguas Extranjeras', 'Lenguas Modernas y Gestión Cultural', 'Letras Hispánicas', 'Letras Modernas', 'Ley del Seguro Social', 'Ley Sarbanes Oxley', 'Licenciatura Internacional en Administración de Centros de Convenciones y Eventos', 'Licenciatura Internacional en Administración de Hoteles y Complejos Turísticos', 'Liderazgo y Gerencia Ambiental', 'Literatura', 'Literatura Latinoamericana', 'Locución y Conducción para Radio y Televisión', 'Logística Internacional', 'Master of Business Administration', 'Matemáticas Aplicadas', 'MBA', 'Mecánica', 'Mecánica y Eléctrica', 'Mecánico Administrador', 'Mecánico Electricista', 'Mecatrónica', 'Mecatrónica y Producción', 'Mediación Familiar', 'Medicina', 'Medicina del Enfermo en Estado Crítico', 'Medicina Interna', 'Medicina Veterinaria y Zootecnia', 'Medico Cirujano', 'Médico Cirujano Odontólogo', 'Médico Homeópata Cirujano y Partero', 'Mercadotecnia', 'Mercadotecnia Deportiva Internacional', 'Mercadotecnia Estratégica', 'Mercadotecnia Estratégica e Innovación', 'Mercadotecnia Internacional', 'Mercadotecnia y Comunicación', 'Mercadotecnia y Estrategia Comercial', 'Mercadotecnia y Publicidad', 'Migración de Sistemas', 'Moda', 'Modelos de Información para la Construcción BIM', 'Modelos Gerenciales', 'Museografía', 'Museología', 'Música', 'Música Contemporánea', 'Nanotecnología y Ciencias Químicas ', 'Negocio de Banquetes', 'Negocios', 'Negocios con Orientación en Hospitalidad', 'Negocios Financieros y Bancarios', 'Negocios Gastronómicos', 'Negocios Internacionales', 'Negocios y Comercial Internacional', 'Negocios y Tecnologías de Información', 'Neonatología', 'Neurolingüística', 'Neurología', 'Neurología Pediátrica', 'Nuevas Estrategias para la Enseñanza de los Estudios Judaicos', 'Nutrición', 'Nutrición Clínica', 'Nutrición Deportiva', 'Nutrición y Bienestar Integral', 'Nutrición y Ciencia de los Alimentos', 'Nutriología Aplicada', 'Obesidad y comorbilidades', 'Obtención de la Certificación ante el Instituto Mexicano de Contadores Públicos', 'Oclusión Orgánica', 'Odontología', 'Odontología cosmética y restaurativa', 'Odontología Legal y Forense', 'Odontopediatría', 'Oftamología', 'Orientación Educativa y Tutoría', 'Orientación Familiar', 'Orientación Psicológica', 'Ortodoncia', 'Ortodoncia Avanzada', 'Ortodoncia Básica', 'Ortodoncia Orgánica', 'Ortopedia Dentofacial', 'Ortopedia Funcional de los Maxilares', 'Pastelería y Panadería', 'Pastoral Familiar', 'Pastoral Urbana', 'Patrimonio Cultural de México', 'Pedagogía', 'Pedagogía Catequética', 'Pedagogía Familiar', 'Pediatría', 'Periodismo', 'Periodismo Cultural', 'Periodismo de Espectáculos', 'Periodismo de Espectáculos y Producción en Televisión', 'Periodismo Económico', 'Periodismo en Fútbol Soccer', 'Periodismo en Sector Justicia y Policíaco', 'Periodismo narrativo y de investigación en prensa, radio y televisión', 'Periodismo Político', 'Periodoncia', 'Photoshop CS5', 'Planeación Estratégica', 'Planeación Estratégica Publicitaria (Planning)', 'Planeación y Desarrollo Turístico', 'Planeación y Gestión Educativa', 'Planeación, Programación y Presupuestación de la Construcción', 'Política Criminal y Seguridad Pública', 'Políticas Públicas', 'Políticas Públicas con Perspectiva de Familia', 'Posgrado', 'Práctico de Impuestos', 'Preescolar', 'Preescolar y Primaria', 'Premiere Pro CS', 'Preparatoria', 'Presupuesto Público', 'Prevención de Violencia Escolar y Familiar', 'Problemática Contemporánea y Ética Social', 'Procedimientos Clínicos y de Laboratorio con guardas oclusales', 'Procuración, Administración de Justicia y Litigación Oral', 'Producción de Televisión', 'Producción Musical Digital', 'Productos Turísticos Sustentables', 'Programación', 'Programador', 'Programas Enfocados', 'Prostodoncia', 'Protección Civil', 'Prótesis Bucal', 'Proyectos para el Desarrollo Urbano', 'Psicoanálisis y Arte', 'Psicología', 'Psicología Clínica', 'Psicología Clínica y de la Salud', 'Psicología Educativa', 'Psicología Organizacional', 'Psicología para Mamás', 'Psicología Social', 'Psicomotricidad', 'Psicopedagogía', 'Psicoterapia', 'Psicoterapia de las Adicciones', 'Psicoterapia Familiar Sistémica', 'Psicoterapia Psicoanalítica', 'Psicoterapia Psicoanalítica con Niños y Adolescentes', 'Psicoterapia Psicoanalítica de Niños', 'Psicoterapia Psicoanalítica Individual', 'Psicoterapia Psicoanalítica Infantil', 'Psiquiatría', 'Publicidad', 'Publicidad Corporativa', 'Publicidad e Imagen', 'Publicidad Integral', 'Publicidad y Comunicación de Mercados', 'Publicidad y Medios', 'Puericultura', 'Química', 'Químico Administrador', 'Químico en Procesos Sustentables', 'Químico Farmacéutico Biólogo', 'Radiología e Imagen', 'Realización Cinematográfica', 'Recursos Humanos', 'Redacción y ortografia', 'Redes de Computadoras', 'Régimen Fiscal de sueldos y salarios', 'Rehabilitación Oral y Odontología Estética', 'Relaciones Económicas', 'Relaciones Internacionales', 'Relaciones Públicas', 'Responsabilidad Social', 'Secretaria Ejecutiva con Computación e Ingles', 'Secretaria en Áreas Comerciales', 'Secretaria en Español e Inglés', 'Secretariado Ejecutivo', 'Secundaria', 'Seguridad de Tecnologías de la Información', 'Seguridad e Higiene en el Trabajo', 'Seguridad e Higiene Industrial', 'Seguridad Pública', 'Serigrafía Textil', 'Servicios Turísticos', 'Sistema Telemática', 'Sistemas Computacionales', 'Sistemas de Calidad y Productividad', 'Sistemas de Computación Administrativa', 'Sistemas de Información', 'Sistemas de Información (Administración de la Tecnología Informática)', 'Sistemas Digitales y Robótica', 'Sistemas Informáticos', 'Sistemas y Tecnologías de la Información', 'Social', 'Sociología', 'Supervisión de Construcción de Edificación', 'Taller de Animación 3D (Autodesk Maya Básico)', 'Taller de Cámara e Iluminación en Video', 'Taller de Comic', 'Taller de Creatividad y Producción de Comerciales', 'Taller de Diseño y Redacción de Anuncios Publicitarios', 'Taller de Efectos Visuales', 'Taller de Excel', 'Taller de Imagen', 'Taller de Lencería y Trajes de Baño', 'Taller de Periodismo de Espectáculos', 'Taller de Photoshop aplicado a la Publicidad', 'Taller de Radio y Televisión, El Poder de la Imaginación y de la Imagen', 'Taller Educación de la Voz, el Sonido de la Personalidad', 'Taller Solicitamos Creativos', 'Tanatología', 'Tanatología y Cuidados Paliativos', 'Teatro', 'Teatro y Actuación', 'Técnica de arco recto de fuerza diferencial con brackets TipEdge Plus', 'Técnicas de Ortodoncia', 'Técnicas y Habilidades Comunicativas', 'Técnico Fiscal Contable', 'Tecnología de Información y Comunicaciones', 'Tecnología Educativa', 'Tecnologías Avanzadas en Educación', 'Tecnologías Computacionales', 'Tecnologías de Cómputo y Telecomunicaciones', 'Tecnologías de Información y Administración', 'Tecnologías de Información y Electrónica', 'Tecnologías de la información', 'Tecnologías de la Información y Telecomunicaciones', 'Tecnologías Electrónicas', 'Telecomunicaciones', 'Telecomunicaciones y Electrónica', 'Telecomunicaciones y Sistemas Electrónicos', 'Teología', 'Teología del Cuerpo', 'Teología y Mundo Contemporáneo', 'Teoría de las Restricciones', 'Teoría Económica', 'Terapia Dentofacial', 'Terapia Física y Rehabilitación', 'Terminología', 'Tomografía Computarizada 3D', 'Topografía y Geomática', 'Traducción', 'Traducción Técnica', 'Traducción Técnica Ingles Español', 'Tráfico de Mercancías y Tramitación Aduanal', 'Turismo', 'Turismo Cultural', 'Turismo Cultural y Cultura Gastronómica', 'Turismo de Reuniones', 'Turismo Internacional', 'Turismo Sustentable', 'Urología', 'Valuación Inmobiliaria', 'Valuación Inmobiliaria e Industrial y de Bienes Nacionales', 'Ventas Inmobiliarias', 'Ventas y Comercialización', 'Vida y pensamiento de Juan Pablo II', 'Video Digital', 'Vinos', 'Vinos y licores para la formación de Sommelier', 'Voz y Dicción']


for study in studiesStringArray:
    customObject = (study,)

    with open('query_result.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for studyNextline in csv_reader:
            # print(studyNextline[0]+"=="+study)
            if(studyNextline[0] == study):
                customObject = customObject + (studyNextline[1],)

    studiesObject.append(customObject)


with open('studies.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(studiesObject)

    writeFile.close()