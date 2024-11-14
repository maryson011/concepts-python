from utils import cliente

job_id = 'ftjob-LhhIeqgyUQIXfAfKGzlp36r9'

# listar jobs
def listat_jobs():
    resposta = cliente.fine_tuning.jobs.list(limit=10)
    print(resposta)
    print('='*50)

# buscar o status de um job
def buscar_job(id):
    resposta = cliente.fine_tuning.jobs.retrieve(id)
    print(resposta)
    print('='*50)

# cancelar um job
def cancelar_job(id):
    resposta = cliente.fine_tuning.jobs.cancel(id)
    print(resposta)
    print('='*50)

# listat_jobs()
buscar_job(job_id)
cancelar_job(job_id)
buscar_job(job_id)