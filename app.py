import streamlit as st
import asyncio
import tempfile
import base64
import os
import subprocess
from datetime import datetime

st.set_page_config(page_title="AI Foundations & Certification Course", layout="wide")

# ---------- Language dictionaries ----------
LANGUAGES = {
    "English": {
        "code": "en",
        "voice": "en-US-GuyNeural",
        "ui": {
            "login_title": "🔐 Access Required",
            "login_sub": "28 days to AI mastery – from beginner to certified expert",
            "login_password": "Enter password to access",
            "login_btn": "Login",
            "login_error": "Incorrect password. Access denied.",
            "sidebar_progress": "Your progress",
            "sidebar_completed": "of 28",
            "sidebar_founder": "Founder & Developer:",
            "sidebar_price_label": "Price",
            "sidebar_price": "$299 USD (full course – all 28 days, source code, certificate)",
            "sidebar_logout": "Logout",
            "day_prefix": "Day",
            "duration_label": "Duration",
            "milestone": "🎯 Milestone achieved! Great progress – keep going!",
            "cert_title": "🏅 Official AI Expert Certificate",
            "cert_text": "Congratulations! You have completed the AI Foundations & Certification Course.",
            "cert_btn": "📜 Download Certificate",
            "congrats_title": "🎓 Congratulations! You are now an AI Certified Expert.",
            "contact_text": "To continue with advanced courses or get support:",
            "footer_caption": "🤖 AI Foundations & Certification Course – 28 days to AI mastery."
        },
        "lessons": {
            1: {"title": "Meet your AI Mentor - Setting up ChatGPT & Gemini", "duration": "15 min", "content": "Learn how to create accounts, navigate the interfaces, and understand the core capabilities of ChatGPT and Google Gemini. These will be your primary AI assistants throughout the course."},
            2: {"title": "The 'Overthinker's Guide' to Prompting - Get exact answers", "duration": "14 min", "content": "Master the art of crafting precise prompts. Discover how to structure questions, use context, and avoid common pitfalls to get exactly the answers you need."},
            3: {"title": "Claude - Brainstorming & organizing messy thoughts", "duration": "16 min", "content": "Explore Claude's strength in handling long context windows. Use it to brainstorm ideas, summarize documents, and organize scattered notes into clear action plans."},
            4: {"title": "Perplexity - Smart, stress-free internet research", "duration": "12 min", "content": "Use Perplexity AI to conduct research with citations. Learn to ask follow-up questions and get accurate, up‑to‑date information without endless searching."},
            5: {"title": "AI for daily productivity & saving 2 hours a day", "duration": "15 min", "content": "Practical ways to integrate AI into your daily routine: email drafting, task prioritization, meeting summaries, and quick data analysis."},
            6: {"title": "Crafting your first custom AI assistant persona", "duration": "18 min", "content": "Create a personalized AI persona tailored to your role or interests. Define its tone, expertise, and typical responses to act as your dedicated assistant."},
            7: {"title": "Milestone - Build your personalized daily AI workflow", "duration": "20 min", "content": "Combine everything from week 1 into a seamless daily routine. Map out when and how you will use each AI tool to maximize efficiency."},
            8: {"title": "MidJourney - Turning simple text into stunning visuals", "duration": "14 min", "content": "Introduction to MidJourney. Learn basic commands, parameters, and how to generate high‑quality images from text prompts."},
            9: {"title": "MidJourney - Creating professional brand graphics", "duration": "16 min", "content": "Advanced techniques: logos, social media banners, presentation backgrounds. Learn to iterate and refine outputs for a consistent brand style."},
            10: {"title": "Canva + AI - Design basics with zero artistic skills", "duration": "15 min", "content": "Use Canva's AI features (Magic Write, Text to Image) to create professional designs quickly. No design experience required."},
            11: {"title": "Runway - Turning static images into engaging video", "duration": "17 min", "content": "Animate static images, add motion, and create short video clips using Runway's Gen‑2 and other tools."},
            12: {"title": "ElevenLabs - Pro voiceovers without recording yourself", "duration": "14 min", "content": "Generate natural‑sounding voiceovers from text. Adjust tone, speed, and emotion to match your project."},
            13: {"title": "Assembling your first AI-generated portfolio piece", "duration": "18 min", "content": "Combine visuals, voiceover, and video into a cohesive portfolio piece. Plan the narrative and structure."},
            14: {"title": "Milestone - Complete your 'Faceless' AI Video Project", "duration": "20 min", "content": "Produce a complete video (e.g., educational short, product promo) using only AI‑generated assets. No on‑camera presence needed."},
            15: {"title": "Basics - Visual automation without a single line of code", "duration": "16 min", "content": "Introduction to automation platforms (Zapier, Make). Understand triggers, actions, and how to connect apps visually."},
            16: {"title": "Connecting AI to your favorite everyday apps", "duration": "18 min", "content": "Integrate AI with Google Sheets, Gmail, Slack, and other common tools to automate repetitive tasks."},
            17: {"title": "Make.com - Building an automated researcher bot", "duration": "15 min", "content": "Step‑by‑step creation of a bot that fetches news, summarizes articles, and sends reports to you on a schedule."},
            18: {"title": "How to present AI wins to your manager", "duration": "18 min", "content": "Frameworks and templates for showcasing your automation successes. Learn to measure ROI and communicate value effectively."},
            19: {"title": "Creating a 24/7 AI Customer Support Agent", "duration": "20 min", "content": "Build a chatbot that answers common customer questions using OpenAI's API or a no‑code platform like Landbot."},
            20: {"title": "Testing & refining your new AI bot", "duration": "15 min", "content": "Methods for testing your bot, collecting feedback, and iterating to improve accuracy and user satisfaction."},
            21: {"title": "Milestone - Deploy your first working AI Automation", "duration": "20 min", "content": "Launch your automation in a real environment (e.g., for your own business or a test project). Document the process and results."},
            22: {"title": "Preparing for your JobEscape AI Certification", "duration": "14 min", "content": "Overview of the certification exam, key topics, and study strategies. Review the official guide."},
            23: {"title": "Packaging your AI skills for your current role", "duration": "16 min", "content": "How to add AI skills to your resume, LinkedIn, and performance reviews. Practical tips for immediate application."},
            24: {"title": "How to present AI wins to your manager (repeat)", "duration": "18 min", "content": "Refine your presentation skills with more examples and role‑play scenarios. Learn to handle questions and objections."},
            25: {"title": "Building your personal AI workflow from scratch", "duration": "15 min", "content": "Design a custom workflow that integrates the tools you've learned. Focus on your unique needs and goals."},
            26: {"title": "The Final AI Knowledge Check & Review", "duration": "20 min", "content": "Comprehensive review of all concepts covered in the course. Practice quiz to test your understanding."},
            27: {"title": "Claim your Official AI Expert Certificate", "duration": "10 min", "content": "Download your personalized certificate after completing the course requirements. Instructions for verification."},
            28: {"title": "Apply what you learned – your first real AI project at work", "duration": "15 min", "content": "Guidance on identifying a real project in your workplace, planning the implementation, and measuring success. Next steps for continued learning."}
        }
    },
    "French": {
        "code": "fr",
        "voice": "fr-FR-HenriNeural",
        "ui": {
            "login_title": "🔐 Accès requis",
            "login_sub": "28 jours pour maîtriser l'IA – du débutant à l'expert certifié",
            "login_password": "Entrez le mot de passe pour accéder",
            "login_btn": "Se connecter",
            "login_error": "Mot de passe incorrect. Accès refusé.",
            "sidebar_progress": "Votre progression",
            "sidebar_completed": "sur 28",
            "sidebar_founder": "Fondateur et développeur :",
            "sidebar_price_label": "Prix",
            "sidebar_price": "299 $ USD (cours complet – 28 jours, code source, certificat)",
            "sidebar_logout": "Déconnexion",
            "day_prefix": "Jour",
            "duration_label": "Durée",
            "milestone": "🎯 Étape clé atteinte ! Bonne continuation !",
            "cert_title": "🏅 Certificat officiel d'expert en IA",
            "cert_text": "Félicitations ! Vous avez terminé le cours « Fondamentaux de l'IA et certification ».",
            "cert_btn": "📜 Télécharger le certificat",
            "congrats_title": "🎓 Félicitations ! Vous êtes désormais un expert certifié en IA.",
            "contact_text": "Pour continuer avec des cours avancés ou obtenir du soutien :",
            "footer_caption": "🤖 Cours « Fondamentaux de l'IA et certification » – 28 jours pour maîtriser l'IA."
        },
        "lessons": {
            1: {"title": "Rencontrez votre mentor IA - Configuration de ChatGPT et Gemini", "duration": "15 min", "content": "Apprenez à créer des comptes, naviguer dans les interfaces et comprendre les capacités de base de ChatGPT et Google Gemini. Ils seront vos principaux assistants IA tout au long du cours."},
            2: {"title": "Le guide du « surpenseur » pour les invites - Obtenez des réponses exactes", "duration": "14 min", "content": "Maîtrisez l'art de formuler des invites précises. Découvrez comment structurer les questions, utiliser le contexte et éviter les pièges courants."},
            3: {"title": "Claude - Brainstorming et organisation des idées", "duration": "16 min", "content": "Exploitez la force de Claude pour gérer de longs contextes. Utilisez-le pour brainstormer, résumer des documents et organiser des notes éparpillées."},
            4: {"title": "Perplexity - Recherche Internet intelligente et sans stress", "duration": "12 min", "content": "Utilisez Perplexity AI pour faire des recherches avec citations. Apprenez à poser des questions de suivi et obtenez des informations précises à jour."},
            5: {"title": "IA pour la productivité quotidienne - Gagnez 2 heures par jour", "duration": "15 min", "content": "Moyens pratiques d'intégrer l'IA dans votre routine : rédaction d'emails, priorisation des tâches, résumés de réunions, analyse rapide de données."},
            6: {"title": "Créez votre premier assistant IA personnalisé", "duration": "18 min", "content": "Créez une personnalité IA adaptée à votre rôle. Définissez son ton, son expertise et ses réponses types."},
            7: {"title": "Étape clé - Construisez votre workflow IA quotidien personnalisé", "duration": "20 min", "content": "Combinez tout ce que vous avez appris pour créer une routine quotidienne fluide."},
            8: {"title": "MidJourney - Transformez du texte en visuels époustouflants", "duration": "14 min", "content": "Introduction à MidJourney. Commandes de base, paramètres, génération d'images de haute qualité."},
            9: {"title": "MidJourney - Créez des graphismes professionnels pour votre marque", "duration": "16 min", "content": "Techniques avancées : logos, bannières sociales, arrière‑plans de présentation."},
            10: {"title": "Canva + IA - Bases du design sans compétences artistiques", "duration": "15 min", "content": "Utilisez les fonctions IA de Canva pour créer des designs professionnels rapidement."},
            11: {"title": "Runway - Animez des images fixes en vidéo", "duration": "17 min", "content": "Animez des images fixes, ajoutez du mouvement, créez des clips courts."},
            12: {"title": "ElevenLabs - Voix off professionnelles sans vous enregistrer", "duration": "14 min", "content": "Générez des voix off naturelles à partir de texte. Ajustez le ton, la vitesse, l'émotion."},
            13: {"title": "Assemblez votre première pièce de portfolio générée par IA", "duration": "18 min", "content": "Combinez visuels, voix off et vidéo en une pièce cohérente."},
            14: {"title": "Étape clé - Projet vidéo IA « sans visage »", "duration": "20 min", "content": "Produisez une vidéo complète en utilisant uniquement des actifs générés par IA."},
            15: {"title": "Bases - Automatisation visuelle sans ligne de code", "duration": "16 min", "content": "Introduction à Zapier et Make : déclencheurs, actions, connexion d'applications."},
            16: {"title": "Connectez l'IA à vos applications quotidiennes", "duration": "18 min", "content": "Intégrez l'IA à Google Sheets, Gmail, Slack, etc."},
            17: {"title": "Make.com - Créez un robot de recherche automatisé", "duration": "15 min", "content": "Bot qui récupère des actualités, résume des articles et envoie des rapports."},
            18: {"title": "Présentez vos succès IA à votre manager", "duration": "18 min", "content": "Modèles pour présenter vos automatisations, mesurer le ROI et communiquer la valeur."},
            19: {"title": "Créez un agent de support client IA 24/7", "duration": "20 min", "content": "Chatbot répondant aux questions courantes via OpenAI ou Landbot."},
            20: {"title": "Testez et améliorez votre nouveau bot IA", "duration": "15 min", "content": "Méthodes de test, collecte de retours, itérations."},
            21: {"title": "Étape clé - Déployez votre première automatisation IA", "duration": "20 min", "content": "Lancez votre automatisation en environnement réel."},
            22: {"title": "Préparez votre certification JobEscape IA", "duration": "14 min", "content": "Aperçu de l'examen, sujets clés, stratégies d'étude."},
            23: {"title": "Valorisez vos compétences IA dans votre rôle actuel", "duration": "16 min", "content": "Ajoutez ces compétences à votre CV, LinkedIn, entretiens."},
            24: {"title": "Présentez vos succès IA à votre manager (répétition)", "duration": "18 min", "content": "Affinez votre présentation avec plus d'exemples."},
            25: {"title": "Construisez votre workflow IA personnel à partir de zéro", "duration": "15 min", "content": "Concevez un workflow personnalisé intégrant les outils appris."},
            26: {"title": "Vérification finale des connaissances IA", "duration": "20 min", "content": "Révision complète de tous les concepts. Quiz pratique."},
            27: {"title": "Obtenez votre certificat officiel d'expert IA", "duration": "10 min", "content": "Téléchargez votre certificat personnalisé après avoir terminé le cours."},
            28: {"title": "Appliquez ce que vous avez appris – premier projet IA réel au travail", "duration": "15 min", "content": "Conseils pour identifier un projet réel, planifier l'implémentation et mesurer le succès."}
        }
    },
    "Spanish": {
        "code": "es",
        "voice": "es-ES-AlvaroNeural",
        "ui": {
            "login_title": "🔐 Acceso requerido",
            "login_sub": "28 días para dominar la IA – de principiante a experto certificado",
            "login_password": "Ingrese la contraseña para acceder",
            "login_btn": "Iniciar sesión",
            "login_error": "Contraseña incorrecta. Acceso denegado.",
            "sidebar_progress": "Tu progreso",
            "sidebar_completed": "de 28",
            "sidebar_founder": "Fundador y desarrollador:",
            "sidebar_price_label": "Precio",
            "sidebar_price": "$299 USD (curso completo – 28 días, código fuente, certificado)",
            "sidebar_logout": "Cerrar sesión",
            "day_prefix": "Día",
            "duration_label": "Duración",
            "milestone": "🎯 ¡Hito alcanzado! Sigue así – ¡buen progreso!",
            "cert_title": "🏅 Certificado oficial de experto en IA",
            "cert_text": "¡Felicitaciones! Has completado el curso «Fundamentos de IA y certificación».",
            "cert_btn": "📜 Descargar certificado",
            "congrats_title": "🎓 ¡Felicitaciones! Ahora eres un experto certificado en IA.",
            "contact_text": "Para continuar con cursos avanzados o recibir apoyo:",
            "footer_caption": "🤖 Curso «Fundamentos de IA y certificación» – 28 días para dominar la IA."
        },
        "lessons": {
            1: {"title": "Conoce a tu mentor IA - Configuración de ChatGPT y Gemini", "duration": "15 min", "content": "Aprende a crear cuentas, navegar por las interfaces y comprender las capacidades básicas de ChatGPT y Google Gemini."},
            2: {"title": "La guía del «sobrepensador» para hacer prompts - Obtén respuestas exactas", "duration": "14 min", "content": "Domina el arte de crear prompts precisos. Estructura preguntas, usa contexto y evita errores comunes."},
            3: {"title": "Claude - Lluvia de ideas y organización de pensamientos", "duration": "16 min", "content": "Explora la fortaleza de Claude para manejar contextos largos. Úsalo para generar ideas, resumir documentos y organizar notas."},
            4: {"title": "Perplexity - Investigación en internet inteligente y sin estrés", "duration": "12 min", "content": "Usa Perplexity AI para investigar con citas. Haz preguntas de seguimiento y obtén información actualizada."},
            5: {"title": "IA para la productividad diaria - Ahorra 2 horas al día", "duration": "15 min", "content": "Formas prácticas de integrar IA en tu rutina: redacción de correos, priorización de tareas, resúmenes de reuniones."},
            6: {"title": "Crea tu primer asistente IA personalizado", "duration": "18 min", "content": "Crea una personalidad IA adaptada a tu rol. Define su tono, experiencia y respuestas típicas."},
            7: {"title": "Hito - Construye tu flujo de trabajo diario con IA", "duration": "20 min", "content": "Combina todo lo aprendido en una rutina diaria fluida."},
            8: {"title": "MidJourney - Convierte texto en imágenes impresionantes", "duration": "14 min", "content": "Introducción a MidJourney. Comandos básicos, parámetros, generación de imágenes de alta calidad."},
            9: {"title": "MidJourney - Crea gráficos profesionales para tu marca", "duration": "16 min", "content": "Técnicas avanzadas: logotipos, banners para redes sociales, fondos de presentaciones."},
            10: {"title": "Canva + IA - Bases del diseño sin habilidades artísticas", "duration": "15 min", "content": "Usa las funciones IA de Canva para crear diseños profesionales rápidamente."},
            11: {"title": "Runway - Convierte imágenes estáticas en video", "duration": "17 min", "content": "Anima imágenes estáticas, añade movimiento, crea clips cortos."},
            12: {"title": "ElevenLabs - Locuciones profesionales sin grabarte", "duration": "14 min", "content": "Genera locuciones naturales a partir de texto. Ajusta tono, velocidad, emoción."},
            13: {"title": "Ensambla tu primera pieza de portafolio generada por IA", "duration": "18 min", "content": "Combina imágenes, locución y video en una pieza coherente."},
            14: {"title": "Hito - Completa tu proyecto de video IA «sin rostro»", "duration": "20 min", "content": "Produce un video completo usando solo activos generados por IA."},
            15: {"title": "Bases - Automatización visual sin una línea de código", "duration": "16 min", "content": "Introducción a Zapier y Make: disparadores, acciones, conexión de aplicaciones."},
            16: {"title": "Conecta IA a tus aplicaciones cotidianas favoritas", "duration": "18 min", "content": "Integra IA con Google Sheets, Gmail, Slack, etc."},
            17: {"title": "Make.com - Construye un bot investigador automatizado", "duration": "15 min", "content": "Bot que obtiene noticias, resume artículos y envía informes programados."},
            18: {"title": "Cómo presentar los logros de IA a tu jefe", "duration": "18 min", "content": "Plantillas para mostrar tus automatizaciones, medir el ROI y comunicar el valor."},
            19: {"title": "Crea un agente de soporte al cliente IA 24/7", "duration": "20 min", "content": "Chatbot que responde preguntas comunes usando OpenAI o Landbot."},
            20: {"title": "Prueba y mejora tu nuevo bot IA", "duration": "15 min", "content": "Métodos para probar, recoger comentarios e iterar."},
            21: {"title": "Hito - Despliega tu primera automatización IA funcional", "duration": "20 min", "content": "Lanza tu automatización en un entorno real."},
            22: {"title": "Prepara tu certificación JobEscape IA", "duration": "14 min", "content": "Resumen del examen, temas clave, estrategias de estudio."},
            23: {"title": "Empaca tus habilidades IA para tu rol actual", "duration": "16 min", "content": "Cómo añadir habilidades IA a tu currículum, LinkedIn y evaluaciones."},
            24: {"title": "Presenta logros IA a tu jefe (repetición)", "duration": "18 min", "content": "Perfecciona tu presentación con más ejemplos."},
            25: {"title": "Construye tu flujo de trabajo IA personal desde cero", "duration": "15 min", "content": "Diseña un flujo de trabajo personalizado que integre las herramientas aprendidas."},
            26: {"title": "Revisión final de conocimientos de IA", "duration": "20 min", "content": "Repaso completo de todos los conceptos. Cuestionario práctico."},
            27: {"title": "Obtén tu certificado oficial de experto en IA", "duration": "10 min", "content": "Descarga tu certificado personalizado después de completar el curso."},
            28: {"title": "Aplica lo aprendido – tu primer proyecto IA real en el trabajo", "duration": "15 min", "content": "Consejos para identificar un proyecto real, planificar la implementación y medir el éxito."}
        }
    },
    "Portuguese": {
        "code": "pt",
        "voice": "pt-BR-FranciscaNeural",
        "ui": {
            "login_title": "🔐 Acesso necessário",
            "login_sub": "28 dias para dominar a IA – do iniciante ao especialista certificado",
            "login_password": "Digite a senha para acessar",
            "login_btn": "Entrar",
            "login_error": "Senha incorreta. Acesso negado.",
            "sidebar_progress": "Seu progresso",
            "sidebar_completed": "de 28",
            "sidebar_founder": "Fundador e desenvolvedor:",
            "sidebar_price_label": "Preço",
            "sidebar_price": "$299 USD (curso completo – 28 dias, código fonte, certificado)",
            "sidebar_logout": "Sair",
            "day_prefix": "Dia",
            "duration_label": "Duração",
            "milestone": "🎯 Meta alcançada! Bom progresso – continue assim!",
            "cert_title": "🏅 Certificado oficial de especialista em IA",
            "cert_text": "Parabéns! Você concluiu o curso «Fundamentos de IA e certificação».",
            "cert_btn": "📜 Baixar certificado",
            "congrats_title": "🎓 Parabéns! Agora você é um especialista certificado em IA.",
            "contact_text": "Para continuar com cursos avançados ou obter suporte:",
            "footer_caption": "🤖 Curso «Fundamentos de IA e certificação» – 28 dias para dominar a IA."
        },
        "lessons": {
            1: {"title": "Conheça seu mentor IA - Configurando ChatGPT e Gemini", "duration": "15 min", "content": "Aprenda a criar contas, navegar pelas interfaces e entender as capacidades básicas do ChatGPT e Google Gemini."},
            2: {"title": "Guia do «pensador excessivo» para prompts - Obtenha respostas exatas", "duration": "14 min", "content": "Domine a arte de criar prompts precisos. Estruture perguntas, use contexto e evite armadilhas comuns."},
            3: {"title": "Claude - Brainstorming e organização de ideias", "duration": "16 min", "content": "Explore a força do Claude em lidar com longos contextos. Use para gerar ideias, resumir documentos e organizar anotações."},
            4: {"title": "Perplexity - Pesquisa na internet inteligente e sem estresse", "duration": "12 min", "content": "Use o Perplexity AI para pesquisar com citações. Faça perguntas de acompanhamento e obtenha informações atualizadas."},
            5: {"title": "IA para produtividade diária - Economize 2 horas por dia", "duration": "15 min", "content": "Formas práticas de integrar IA à sua rotina: redação de e-mails, priorização de tarefas, resumos de reuniões."},
            6: {"title": "Crie seu primeiro assistente IA personalizado", "duration": "18 min", "content": "Crie uma persona IA adaptada ao seu papel. Defina tom, expertise e respostas típicas."},
            7: {"title": "Marco - Construa seu fluxo de trabalho diário com IA", "duration": "20 min", "content": "Combine tudo o que aprendeu em uma rotina diária perfeita."},
            8: {"title": "MidJourney - Transforme texto em visuais impressionantes", "duration": "14 min", "content": "Introdução ao MidJourney. Comandos básicos, parâmetros, geração de imagens de alta qualidade."},
            9: {"title": "MidJourney - Crie gráficos profissionais para sua marca", "duration": "16 min", "content": "Técnicas avançadas: logotipos, banners para redes sociais, fundos de apresentação."},
            10: {"title": "Canva + IA - Noções básicas de design sem habilidades artísticas", "duration": "15 min", "content": "Use os recursos de IA do Canva para criar designs profissionais rapidamente."},
            11: {"title": "Runway - Transforme imagens estáticas em vídeo", "duration": "17 min", "content": "Anime imagens estáticas, adicione movimento, crie clipes curtos."},
            12: {"title": "ElevenLabs - Narrações profissionais sem se gravar", "duration": "14 min", "content": "Gere narrações naturais a partir de texto. Ajuste tom, velocidade, emoção."},
            13: {"title": "Monte sua primeira peça de portfólio gerada por IA", "duration": "18 min", "content": "Combine visuais, narração e vídeo em uma peça coesa."},
            14: {"title": "Marco - Complete seu projeto de vídeo IA «sem rosto»", "duration": "20 min", "content": "Produza um vídeo completo usando apenas ativos gerados por IA."},
            15: {"title": "Bases - Automação visual sem uma linha de código", "duration": "16 min", "content": "Introdução ao Zapier e Make: gatilhos, ações, conexão de aplicativos."},
            16: {"title": "Conecte IA aos seus aplicativos diários favoritos", "duration": "18 min", "content": "Integre IA com Google Sheets, Gmail, Slack e outras ferramentas."},
            17: {"title": "Make.com - Construa um bot pesquisador automatizado", "duration": "15 min", "content": "Bot que obtém notícias, resume artigos e envia relatórios agendados."},
            18: {"title": "Como apresentar vitórias da IA ao seu gerente", "duration": "18 min", "content": "Modelos para mostrar suas automações, medir ROI e comunicar valor."},
            19: {"title": "Crie um agente de suporte ao cliente IA 24/7", "duration": "20 min", "content": "Chatbot que responde perguntas comuns usando OpenAI ou Landbot."},
            20: {"title": "Teste e refine seu novo bot IA", "duration": "15 min", "content": "Métodos para testar, coletar feedback e iterar."},
            21: {"title": "Marco - Implante sua primeira automação IA funcional", "duration": "20 min", "content": "Lance sua automação em um ambiente real."},
            22: {"title": "Prepare-se para sua certificação JobEscape IA", "duration": "14 min", "content": "Visão geral do exame, tópicos principais, estratégias de estudo."},
            23: {"title": "Empacote suas habilidades de IA para sua função atual", "duration": "16 min", "content": "Como adicionar habilidades de IA ao seu currículo, LinkedIn e avaliações."},
            24: {"title": "Apresente vitórias da IA ao seu gerente (repetição)", "duration": "18 min", "content": "Aprimore sua apresentação com mais exemplos."},
            25: {"title": "Construa seu fluxo de trabalho IA pessoal do zero", "duration": "15 min", "content": "Projete um fluxo de trabalho personalizado que integre as ferramentas aprendidas."},
            26: {"title": "Verificação final de conhecimento em IA", "duration": "20 min", "content": "Revisão abrangente de todos os conceitos. Questionário prático."},
            27: {"title": "Obtenha seu certificado oficial de especialista em IA", "duration": "10 min", "content": "Baixe seu certificado personalizado após concluir o curso."},
            28: {"title": "Aplique o que aprendeu – seu primeiro projeto real de IA no trabalho", "duration": "15 min", "content": "Orientações para identificar um projeto real, planejar a implementação e medir o sucesso."}
        }
    }
}

# ---------- Helper functions ----------
def set_tech_style():
    st.markdown("""
        <style>
        .stApp { background: linear-gradient(135deg, #0a0f1f, #0e1a2a, #0a0f1f); }
        .main-header { background: linear-gradient(135deg, #00d4ff, #0077ff, #0033aa); padding: 1.5rem; border-radius: 20px; text-align: center; margin-bottom: 1rem; }
        .main-header h1 { color: white; text-shadow: 2px 2px 4px #000000; font-size: 2.5rem; margin: 0; }
        .main-header p { color: #fff5cc; font-size: 1.2rem; margin: 0; }
        html, body, .stApp, .stMarkdown, .stText, .stRadio label, .stSelectbox label, .stTextInput label, .stButton button, .stTitle, .stSubheader, .stHeader, .stCaption, .stAlert, .stException, .stCodeBlock, .stDataFrame, .stTable, .stTabs [role="tab"], .stTabs [role="tablist"] button, .stExpander, .stProgress > div, .stMetric label, .stMetric value, div, p, span, pre, code, .element-container, .stTextArea label, .stText p, .stText div, .stText span, .stText code { color: #ffffff !important; }
        .stText { color: #ffffff !important; font-size: 1rem; background: transparent !important; }
        .stTabs [role="tab"] { color: #ffffff !important; background: rgba(0,212,255,0.2); border-radius: 10px; margin: 0 2px; }
        .stTabs [role="tab"][aria-selected="true"] { background: #0077ff; color: white !important; }
        .stRadio [role="radiogroup"] label { background: rgba(255,255,255,0.1); border-radius: 10px; padding: 0.3rem; margin: 0.2rem 0; color: white !important; }
        .stButton button { background-color: #0077ff; color: white !important; border-radius: 30px; font-weight: bold; }
        .stButton button:hover { background-color: #00d4ff; color: black !important; }
        section[data-testid="stSidebar"] { background: linear-gradient(135deg, #0a0f1f, #0e1a2a); }
        section[data-testid="stSidebar"] .stMarkdown, section[data-testid="stSidebar"] .stText, section[data-testid="stSidebar"] label { color: white !important; }
        section[data-testid="stSidebar"] .stSelectbox label { color: white !important; }
        section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] { background-color: #1e2a3a; border: 1px solid #0077ff; border-radius: 10px; }
        div[data-baseweb="popover"] ul { background-color: #1e2a3a; border: 1px solid #0077ff; }
        div[data-baseweb="popover"] li { color: white !important; background-color: #1e2a3a; }
        div[data-baseweb="popover"] li:hover { background-color: #0077ff; }
        .certificate { background: linear-gradient(135deg, #ffd700, #ffaa00); padding: 1rem; border-radius: 20px; text-align: center; color: #000 !important; }
        .certificate h3, .certificate p { color: #000 !important; }
        </style>
    """, unsafe_allow_html=True)

def show_logo():
    st.markdown("""
        <div style="display: flex; justify-content: center; margin-bottom: 1rem;">
            <svg width="100" height="100" viewBox="0 0 100 100">
                <circle cx="50" cy="50" r="45" fill="url(#gradLogo)" stroke="#00d4ff" stroke-width="3"/>
                <defs><linearGradient id="gradLogo" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="#00d4ff"/>
                    <stop offset="50%" stop-color="#0077ff"/>
                    <stop offset="100%" stop-color="#0033aa"/>
                </linearGradient></defs>
                <text x="50" y="65" font-size="40" text-anchor="middle" fill="white" font-weight="bold">🤖</text>
            </svg>
        </div>
    """, unsafe_allow_html=True)

def generate_audio(text, output_path, voice):
    cmd = ["edge-tts", "--voice", voice, "--text", text, "--write-media", output_path]
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True, timeout=30)
    except Exception as e:
        st.error(f"Audio error: {e}")

def play_audio(text, key, voice):
    if st.button(f"🔊", key=key):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
            generate_audio(text, tmp.name, voice)
            with open(tmp.name, "rb") as f:
                audio_bytes = f.read()
                b64 = base64.b64encode(audio_bytes).decode()
                st.markdown(f'<audio controls src="data:audio/mp3;base64,{b64}" autoplay style="width: 100%;"></audio>', unsafe_allow_html=True)
            os.unlink(tmp.name)

# ---------- Authentication ----------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "lang" not in st.session_state:
    st.session_state.lang = "English"

def set_language():
    pass

if not st.session_state.authenticated:
    set_tech_style()
    st.title("🔐 Access Required")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        show_logo()
        st.markdown("<h2 style='text-align: center;'>AI Foundations & Certification Course</h2>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; color: #00d4ff;'>{LANGUAGES[st.session_state.lang]['ui']['login_sub']}</p>", unsafe_allow_html=True)
        password_input = st.text_input(LANGUAGES[st.session_state.lang]['ui']['login_password'], type="password")
        if st.button(LANGUAGES[st.session_state.lang]['ui']['login_btn']):
            if password_input == "20082010":
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error(LANGUAGES[st.session_state.lang]['ui']['login_error'])
    st.stop()

# ---------- Main app after login ----------
set_tech_style()
with st.sidebar:
    st.image("https://flagcdn.com/w320/ht.png", width=60)
    st.selectbox("🌐 Language", options=list(LANGUAGES.keys()), key="lang", on_change=set_language)
    st.markdown("---")
    show_logo()
    st.markdown(f"## 🎯 {LANGUAGES[st.session_state.lang]['ui']['day_prefix']}")
    day_number = st.selectbox("", list(range(1, 29)), index=0, label_visibility="collapsed")
    st.markdown("---")
    st.markdown(f"### 📚 {LANGUAGES[st.session_state.lang]['ui']['sidebar_progress']}")
    st.progress(day_number / 28)
    st.markdown(f"✅ {LANGUAGES[st.session_state.lang]['ui']['day_prefix']} {day_number} {LANGUAGES[st.session_state.lang]['ui']['sidebar_completed']}")
    st.markdown("---")
    st.markdown(f"**{LANGUAGES[st.session_state.lang]['ui']['sidebar_founder']}**")
    st.markdown("Gesner Deslandes")
    st.markdown("📞 WhatsApp: (509) 4738-5663")
    st.markdown("📧 Email: deslandes78@gmail.com")
    st.markdown("🌐 [Main website](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/)")
    st.markdown("---")
    st.markdown(f"### 💰 {LANGUAGES[st.session_state.lang]['ui']['sidebar_price_label']}")
    st.markdown(LANGUAGES[st.session_state.lang]['ui']['sidebar_price'])
    st.markdown("---")
    st.markdown("### © 2025 GlobalInternet.py")
    st.markdown("All rights reserved")
    st.markdown("---")
    if st.button(f"🚪 {LANGUAGES[st.session_state.lang]['ui']['sidebar_logout']}", use_container_width=True):
        st.session_state.authenticated = False
        st.rerun()

# ---------- Display current lesson ----------
lang = st.session_state.lang
ui = LANGUAGES[lang]["ui"]
voice = LANGUAGES[lang]["voice"]
lessons = LANGUAGES[lang]["lessons"]

week_num = (day_number - 1) // 7 + 1
week_titles = {
    1: "Week 1 - AI Foundations & Your Personal Mentor",
    2: "Week 2 - Creativity & Quiet Skill-Building",
    3: "Week 3 - Building AI Bots & Smart Automation",
    4: "Week 4 - Certification & Career Application"
}
week_title = week_titles[week_num]

day_title = lessons[day_number]["title"]
duration = lessons[day_number]["duration"]
content = lessons[day_number]["content"]

st.markdown(f"## 📅 {week_title}")
st.markdown(f"### {ui['day_prefix']} {day_number}: {day_title}")
st.markdown(f"⏱️ **{ui['duration_label']}:** {duration}")
st.markdown("---")
st.markdown(content)

# Audio for the lesson content
play_audio(f"{ui['day_prefix']} {day_number}: {day_title}. {content}", f"audio_{day_number}_{lang}", voice)

# Milestone indicator
if day_number in [7, 14, 21, 28]:
    st.markdown("---")
    st.success(ui['milestone'])

# Certificate claim on day 27-28
if day_number >= 27:
    st.markdown("---")
    st.markdown(f'<div class="certificate"><h3>{ui["cert_title"]}</h3><p>{ui["cert_text"]}</p><p>Click the button below to download your certificate.</p></div>', unsafe_allow_html=True)
    if st.button(ui['cert_btn'], use_container_width=True):
        cert_text = f"AI Expert Certificate\n\nThis certifies that User has successfully completed the 28‑day AI Foundations & Certification Course.\n\nDate: {datetime.now().strftime('%Y-%m-%d')}\n\nGesner Deslandes\nFounder, GlobalInternet.py"
        st.download_button("⬇️ Download Certificate (TXT)", cert_text, file_name="ai_certificate.txt", mime="text/plain")

if day_number == 28:
    st.markdown("---")
    st.markdown(f"## {ui['congrats_title']}")
    st.markdown(f"""
    ### 📞 {ui['contact_text']}
    - **Gesner Deslandes** – Founder
    - 📱 WhatsApp: (509) 4738-5663
    - 📧 Email: deslandes78@gmail.com
    - 🌐 [GlobalInternet.py](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/)
    
    Keep practicing and applying your skills. You are ready for real‑world AI projects!
    """)

st.markdown("---")
st.caption(ui['footer_caption'])
