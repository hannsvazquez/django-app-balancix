from django.db import models

# Defining the choices for internships

class InternshipOffers(models.Model):
    TYPE_OF_OFFERS = [
        ('FT', 'Full-Time'),
        ('PT', 'Part-Time'),
        ('PR', 'Project-Based')
    ]


    position = models.CharField("Posición", max_length=255)

    type_of_job = models.CharField(
        "Tipo de oportunidad",
        max_length=2,
        choices=TYPE_OF_OFFERS
    )

    duration = models.CharField("Duración", max_length=100)

    date_limit = models.DateField("Fecha límite")

    brief_description = models.TextField("Descripción")

    location = models.CharField("País / Localidad", max_length=255)

    company = models.ForeignKey(
        'Companies',
        verbose_name="Empresa",
        on_delete=models.CASCADE,
        related_name="internship_offers",
        default=1
    )

    banner = models.ImageField(
        "Banner de la oferta",
        upload_to='internship_banners/',
        help_text="Imagen banner para cada oferta que se muestre en el dashboard"
    )

    ai_recommendation = models.TextField(
        "Recomendaciones generadas por IA",
        blank=True,
        null=True
    )
    mentors = models.ManyToManyField(
        'Mentor',  # Use string reference to avoid circular import
        verbose_name="Mentor",
        blank=True
    )
    

    created_at = models.DateTimeField("Fecha de publicación", auto_now_add=True)

    def __str__(self):
        return f"{self.position} en {self.company.name}"


# Defining fields for the company
class Companies(models.Model):

    STAGE_OPTIONS = [
        ('PS', 'Pre-seed'),
        ('SEED', 'Seed'),
        ('SA', 'Serie A'),
        ('SB', 'Serie B'),
        ('SC', 'Serie C'),
        ('PYME', 'Pequeño Negocio'),
        ('ENT', 'Enterprise')
    ]

    INDUSTRY_OPTIONS = [
        ('WEB3', 'Web3 & Blockchain'),
        ('FIN', 'Financial Services'),
        ('ENT_SOFT', 'Enterprise Software'),
        ('HEALTH', 'Healthcare & Biotech'),
        ('EDU', 'Education & EdTech'),
        ('ECOMM', 'E-commerce & Retail'),
        ('AI_ML', 'Artificial Intelligence & Machine Learning'),
        ('MOBILITY', 'Mobility & Transportation'),
        ('REAL_ESTATE', 'Real Estate & PropTech'),
        ('MEDIA', 'Media & Entertainment'),
        ('HR_TECH', 'HR & Recruitment'),
        ('MARKETING', 'Marketing & Advertising'),
        ('LOGISTICS', 'Logistics & Supply Chain'),
        ('FOOD','FoodTech'),
        ('CREAECON', 'Creator Economy'),
        ('OTHER', 'Other'),
    ]

    name = models.CharField("Nombre de la empresa", max_length=250)
    website = models.URLField("Sitio Web", blank=True, null=True)
    description = models.TextField("Descripción", blank=True, null=True)

    stage = models.CharField(
        "Etapa de la empresa",
        max_length=10,
        choices=STAGE_OPTIONS,
        default='SA'
    )
    industry = models.CharField(
        "Industria",
        max_length=20,
        choices=INDUSTRY_OPTIONS,
        default='ENT_SOFT'
    )

    def __str__(self):
        return self.name


class Mentor(models.Model):
    full_name = models.CharField("Nombre completo", max_length=255)
    role = models.CharField("Rol o cargo", max_length=255, blank=True, null=True)
    linkedin_url = models.URLField("Perfil de LinkedIn", blank=True, null=True)

    
    # Nuevo: Conexión del mentor con una empresa
    company = models.ForeignKey(
        Companies,
        verbose_name="Empresa del mentor",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="mentors"
    )

    def __str__(self):
        return self.full_name
    

