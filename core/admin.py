from django.contrib import admin
from .models import ProjetoBecIndicador, ProjetoBpmIndicador, ProjetoCoeticIndicador
from .models import ProjetoDatacenterIndicador, ProjetoDoIndicador, ProjetoGovbrIndicador
from .models import ProjetoPortalspIndicador, ProjetoSeducIndicador, ProjetoSegurancainfIndicador 
from .models import ProjetoSeiIndicador, ProjetoSneIndicador, ProjetoSouIndicador
from .models import Projetotipoperiodicidade, Projetotipounidade, Projetoindicador

admin.site.register(ProjetoBecIndicador)
admin.site.register(ProjetoBpmIndicador)
admin.site.register(ProjetoCoeticIndicador)
admin.site.register(ProjetoDatacenterIndicador)
admin.site.register(ProjetoDoIndicador)
admin.site.register(ProjetoGovbrIndicador)
admin.site.register(ProjetoPortalspIndicador)
admin.site.register(ProjetoSeducIndicador)
admin.site.register(ProjetoSegurancainfIndicador)
admin.site.register(ProjetoSeiIndicador)
admin.site.register(ProjetoSneIndicador)
admin.site.register(ProjetoSouIndicador)
admin.site.register(Projetotipoperiodicidade)
admin.site.register(Projetotipounidade)
admin.site.register(Projetoindicador)

# Register your models here.
# ALTERA NOMENCLATURA DO ADMIN PAGE.
admin.site.site_header = "Projetos"
admin.site.site_title = "Projetos Portal"
#admin.site.index_title = "Welcome to UMSRA Researcher Portal"
