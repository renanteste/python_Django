# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Projeto(models.Model):
    idprojeto = models.BigIntegerField(primary_key=True)
    areagestora = models.CharField(db_column='AreaGestora', max_length=200, blank=True, null=True)  # Field name made lowercase.
    projeto = models.CharField(db_column='Projeto', max_length=200, blank=True, null=True)  # Field name made lowercase.
    alinhamentoestrategico = models.CharField(db_column='AlinhamentoEstrategico', max_length=200, blank=True, null=True)  # Field name made lowercase.
    publicoalvo = models.CharField(db_column='PublicoAlvo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    justificativa = models.CharField(db_column='Justificativa', max_length=200, blank=True, null=True)  # Field name made lowercase.
    stajeholder = models.CharField(db_column='Stajeholder', max_length=200, blank=True, null=True)  # Field name made lowercase.
    objetivo = models.CharField(db_column='Objetivo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    prazo = models.DateField(db_column='Prazo', blank=True, null=True)  # Field name made lowercase.
    custo = models.DecimalField(db_column='Custo', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    restricoes = models.CharField(db_column='Restricoes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    requisitos = models.CharField(db_column='Requisitos', max_length=200, blank=True, null=True)  # Field name made lowercase.
    principaisriscos = models.CharField(db_column='PrincipaisRiscos', max_length=200, blank=True, null=True)  # Field name made lowercase.
    entregaveis = models.CharField(db_column='Entregaveis', max_length=200, blank=True, null=True)  # Field name made lowercase.
    beneficios = models.CharField(db_column='Beneficios', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rebulamentacao = models.CharField(db_column='Rebulamentacao', max_length=200, blank=True, null=True)  # Field name made lowercase.
    datainclusao = models.DateTimeField()
    dataalteracao = models.DateTimeField()
    idusuariocriacao = models.BigIntegerField()
    idusuarioalteracao = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'Projeto'


class Projetoindicador(models.Model):
    idprojeto = models.BigIntegerField(primary_key=True)
    idprojetoindicador = models.CharField(db_column='idprojetoIndicador', max_length=36)  # Field name made lowercase.
    formulacalculo = models.CharField(db_column='FormulaCalculo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    idprojetotipounidade = models.IntegerField(db_column='idprojetoTipoUnidade', blank=True, null=True)  # Field name made lowercase.
    idprojetotipoperiodicidade = models.IntegerField(db_column='idprojetoTipoPeriodicidade', blank=True, null=True)  # Field name made lowercase.
    duracaoreporte = models.IntegerField(db_column='DuracaoReporte', blank=True, null=True)  # Field name made lowercase.
    alinhamentoestrategico = models.CharField(db_column='AlinhamentoEstrategico', max_length=200, blank=True, null=True)  # Field name made lowercase.
    publicoalvo = models.CharField(db_column='PublicoAlvo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    justificativa = models.CharField(db_column='Justificativa', max_length=200, blank=True, null=True)  # Field name made lowercase.
    stajeholder = models.CharField(db_column='Stajeholder', max_length=200, blank=True, null=True)  # Field name made lowercase.
    objetivo = models.CharField(db_column='Objetivo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    prazo = models.DateField(db_column='Prazo', blank=True, null=True)  # Field name made lowercase.
    custo = models.DecimalField(db_column='Custo', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    restricoes = models.CharField(db_column='Restricoes', max_length=200, blank=True, null=True)  # Field name made lowercase.
    requisitos = models.CharField(db_column='Requisitos', max_length=200, blank=True, null=True)  # Field name made lowercase.
    principaisriscos = models.CharField(db_column='PrincipaisRiscos', max_length=200, blank=True, null=True)  # Field name made lowercase.
    entregaveis = models.CharField(db_column='Entregaveis', max_length=200, blank=True, null=True)  # Field name made lowercase.
    beneficios = models.CharField(db_column='Beneficios', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rebulamentacao = models.CharField(db_column='Rebulamentacao', max_length=200, blank=True, null=True)  # Field name made lowercase.
    datainclusao = models.DateTimeField()
    dataalteracao = models.DateTimeField()
    idusuariocriacao = models.BigIntegerField()
    idusuarioalteracao = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'ProjetoIndicador'
        unique_together = (('idprojeto', 'idprojetoindicador'),)


class Projetotipoperiodicidade(models.Model):
    idprojetotipoperiodicidade = models.IntegerField(db_column='idprojetoTipoPeriodicidade', primary_key=True)  # Field name made lowercase.
    tipoperiodicidade = models.CharField(db_column='TipoPeriodicidade', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProjetoTipoPeriodicidade'


class Projetotipounidade(models.Model):
    idprojetotipounidade = models.IntegerField(db_column='idprojetoTipoUnidade', primary_key=True)  # Field name made lowercase.
    tipounidademedida = models.CharField(db_column='TipoUnidadeMedida', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProjetoTipoUnidade'


class ProjetoBecIndicador(models.Model):
    idgbecindicador = models.CharField(db_column='idGBECIndicador', primary_key=True, max_length=36)  # Field name made lowercase.
    idprojeto = models.BigIntegerField()
    qtddownloadandroid = models.BigIntegerField(db_column='QtdDownloadAndroid', blank=True, null=True)  # Field name made lowercase.
    qtddownloaios = models.BigIntegerField(db_column='QtdDownloaIOS', blank=True, null=True)  # Field name made lowercase.
    acessossemanal = models.BigIntegerField(db_column='AcessosSemanal', blank=True, null=True)  # Field name made lowercase.
    servidoresdistintos = models.BigIntegerField(db_column='ServidoresDistintos', blank=True, null=True)  # Field name made lowercase.
    boativo = models.BooleanField(db_column='boAtivo', blank=True, null=True)  # Field name made lowercase.
    datainclusao = models.DateTimeField()
    dataalteracao = models.DateTimeField()
    idusuarioa = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'Projeto_BEC_Indicador'


class ProjetoBpmIndicador(models.Model):
    idbpmindicador = models.CharField(db_column='idBPMIndicador', primary_key=True, max_length=36)  # Field name made lowercase.
    idprojeto = models.BigIntegerField()
    economiacustoservico = models.DecimalField(db_column='EconomiaCustoServico', max_digits=16, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tempoexecucaoservico = models.DecimalField(db_column='TempoExecucaoServico', max_digits=16, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    comparacaohumanosxdigital = models.DecimalField(db_column='ComparacaoHumanosXDigital', max_digits=16, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    boativo = models.BooleanField(db_column='boAtivo', blank=True, null=True)  # Field name made lowercase.
    datainclusao = models.DateTimeField()
    dataalteracao = models.DateTimeField()
    idusuarioa = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'Projeto_BPM_Indicador'


class ProjetoCoeticIndicador(models.Model):
    idcoeticindicador = models.CharField(db_column='idCOETICIndicador', primary_key=True, max_length=36)  # Field name made lowercase.
    idprojeto = models.BigIntegerField()
    demandanormaisvalor = models.DecimalField(db_column='DemandaNormaisValor', max_digits=16, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    demandanormaisqtd = models.BigIntegerField(db_column='DemandaNormaisQtd', blank=True, null=True)  # Field name made lowercase.
    demandaadnormaisvalor = models.DecimalField(db_column='DemandaAdNormaisValor', max_digits=16, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    demandaadnormaisqtd = models.BigIntegerField(db_column='DemandaAdNormaisQtd', blank=True, null=True)  # Field name made lowercase.
    boativo = models.BooleanField(db_column='boAtivo', blank=True, null=True)  # Field name made lowercase.
    datainclusao = models.DateTimeField()
    dataalteracao = models.DateTimeField()
    idusuarioa = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'Projeto_COETIC_Indicador'


class ProjetoDoIndicador(models.Model):
    iddondicador = models.CharField(db_column='idDOndicador', primary_key=True, max_length=36)  # Field name made lowercase.
    idprojeto = models.BigIntegerField()
    mediapesquisadiaria = models.DecimalField(db_column='MediaPesquisaDiaria', max_digits=16, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    consultausuario = models.DecimalField(db_column='ConsultaUsuario', max_digits=16, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    consultaedicaodia = models.DecimalField(db_column='ConsultaEdicaoDia', max_digits=16, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tempomediopermanenciasite = models.DecimalField(db_column='TempoMedioPermanenciaSite', max_digits=16, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    boativo = models.BooleanField(db_column='boAtivo', blank=True, null=True)  # Field name made lowercase.
    datainclusao = models.DateTimeField()
    dataalteracao = models.DateTimeField()
    idusuarioa = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'Projeto_DO_Indicador'


class ProjetoDatacenterIndicador(models.Model):
    iddatacenterindicador = models.CharField(db_column='idDataCenterIndicador', primary_key=True, max_length=36)  # Field name made lowercase.
    idprojeto = models.BigIntegerField()
    certificacaotier3 = models.DecimalField(db_column='CertificacaoTier3', max_digits=16, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    disasterrecovery = models.DecimalField(db_column='DisasterRecovery', max_digits=16, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    boativo = models.BooleanField(db_column='boAtivo', blank=True, null=True)  # Field name made lowercase.
    datainclusao = models.DateTimeField()
    dataalteracao = models.DateTimeField()
    idusuarioa = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'Projeto_DataCenter_Indicador'


class ProjetoGovbrIndicador(models.Model):
    idgovbrindicador = models.CharField(db_column='idGOVBRIndicador', primary_key=True, max_length=36)  # Field name made lowercase.
    idprojeto = models.BigIntegerField()
    migracaosistema = models.IntegerField(db_column='MigracaoSistema', blank=True, null=True)  # Field name made lowercase.
    implementacaoecosistemaidp = models.IntegerField(db_column='ImplementacaoEcosistemaIDP', blank=True, null=True)  # Field name made lowercase.
    boativo = models.BooleanField(db_column='boAtivo', blank=True, null=True)  # Field name made lowercase.
    datainclusao = models.DateTimeField()
    dataalteracao = models.DateTimeField()
    idusuarioa = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'Projeto_GOVBR_Indicador'


class ProjetoPortalspIndicador(models.Model):
    idportalspindicador = models.CharField(db_column='idPortalSPIndicador', primary_key=True, max_length=36)  # Field name made lowercase.
    idprojeto = models.BigIntegerField()
    taxacrescimentousuario = models.DecimalField(db_column='TaxaCrescimentoUsuario', max_digits=16, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    notavaliacaolojaapp = models.BigIntegerField(db_column='NotaValiacaoLojaApp', blank=True, null=True)  # Field name made lowercase.
    roi = models.DecimalField(db_column='ROI', max_digits=16, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    taxaretencao = models.DecimalField(db_column='TaxaRetencao', max_digits=16, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    boativo = models.BooleanField(db_column='boAtivo', blank=True, null=True)  # Field name made lowercase.
    datainclusao = models.DateTimeField()
    dataalteracao = models.DateTimeField()
    idusuarioa = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'Projeto_PortalSP_Indicador'


class ProjetoSeiIndicador(models.Model):
    idseiindicador = models.CharField(db_column='idSEIIndicador', primary_key=True, max_length=36)  # Field name made lowercase.
    idprojeto = models.BigIntegerField()
    documentosgerados = models.IntegerField(db_column='DocumentosGerados', blank=True, null=True)  # Field name made lowercase.
    processoscriados = models.IntegerField(db_column='ProcessosCriados', blank=True, null=True)  # Field name made lowercase.
    boativo = models.BooleanField(db_column='boAtivo', blank=True, null=True)  # Field name made lowercase.
    datainclusao = models.DateTimeField()
    dataalteracao = models.DateTimeField()
    idusuarioa = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'Projeto_SEI_Indicador'


class ProjetoSneIndicador(models.Model):
    idsneindicador = models.CharField(db_column='idSneIndicador', primary_key=True, max_length=36)  # Field name made lowercase.
    idprojeto = models.BigIntegerField()
    descontosolicitado = models.DecimalField(db_column='DescontoSolicitado', max_digits=16, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    multaspagas = models.DecimalField(db_column='MultasPagas', max_digits=16, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valoreconomizado = models.DecimalField(db_column='ValorEconomizado', max_digits=16, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    boativo = models.BooleanField(db_column='boAtivo', blank=True, null=True)  # Field name made lowercase.
    datainclusao = models.DateTimeField()
    dataalteracao = models.DateTimeField()
    idusuarioa = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'Projeto_SNE_Indicador'


class ProjetoSouIndicador(models.Model):
    idgsouindicador = models.CharField(db_column='idGSOUIndicador', primary_key=True, max_length=36)  # Field name made lowercase.
    idprojeto = models.BigIntegerField()
    qtddownloadandroid = models.BigIntegerField(db_column='QtdDownloadAndroid', blank=True, null=True)  # Field name made lowercase.
    qtddownloaios = models.BigIntegerField(db_column='QtdDownloaIOS', blank=True, null=True)  # Field name made lowercase.
    acessossemanal = models.BigIntegerField(db_column='AcessosSemanal', blank=True, null=True)  # Field name made lowercase.
    servidoresdistintos = models.BigIntegerField(db_column='ServidoresDistintos', blank=True, null=True)  # Field name made lowercase.
    boativo = models.BooleanField(db_column='boAtivo', blank=True, null=True)  # Field name made lowercase.
    datainclusao = models.DateTimeField()
    dataalteracao = models.DateTimeField()
    idusuarioa = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'Projeto_SOU_Indicador'


class ProjetoSeducIndicador(models.Model):
    idseducindicador = models.CharField(db_column='idSeducIndicador', primary_key=True, max_length=36)  # Field name made lowercase.
    idprojeto = models.BigIntegerField()
    numeroprovas = models.BigIntegerField(db_column='NumeroProvas', blank=True, null=True)  # Field name made lowercase.
    numeroalunos = models.BigIntegerField(db_column='NumeroAlunos', blank=True, null=True)  # Field name made lowercase.
    boativo = models.BooleanField(db_column='boAtivo', blank=True, null=True)  # Field name made lowercase.
    datainclusao = models.DateTimeField()
    dataalteracao = models.DateTimeField()
    idusuarioa = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'Projeto_Seduc_Indicador'


class ProjetoSegurancainfIndicador(models.Model):
    idgsegurancainfindicador = models.CharField(db_column='idGSegurancaInfIndicador', primary_key=True, max_length=36)  # Field name made lowercase.
    idprojeto = models.BigIntegerField()
    ataquesbloqueadosfirewall = models.BigIntegerField(db_column='AtaquesBloqueadosFirewall', blank=True, null=True)  # Field name made lowercase.
    ataquesbloqueadosips = models.BigIntegerField(db_column='AtaquesBloqueadosIPS', blank=True, null=True)  # Field name made lowercase.
    boativo = models.BooleanField(db_column='boAtivo', blank=True, null=True)  # Field name made lowercase.
    datainclusao = models.DateTimeField()
    dataalteracao = models.DateTimeField()
    idusuarioa = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'Projeto_SegurancaInf_Indicador'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
