import kfp 
from kfp import dsl
import kfp.compiler
import kfp.compiler.compiler


### Componentes of pipeline
def data_processing_op():
    return dsl.ContainerOp(
        name="Data Processing",
        image="ambuj6392/my-mlops-app",
        command=["python","src/data_processing.py"]
    )

def model_training_op():
    return dsl.ContainerOp(
        name="Model Training",
        image="ambuj6392/my-mlops-app",
        command=["python","src/model_training.py"]
    )

### pipeline starts here...
@dsl.pipeline(
    name="MLOPS Pipeline",
    description="This is my first kubeflow pipeline"
)

def mlops_pipeline():
    data_processing = data_processing_op()
    model_training = model_training_op().after(data_processing)

### Run Pipeline
if __name__=="__main__":
    kfp.compiler.Compiler().compile(
        mlops_pipeline, "mlops_pipeline.yaml"
    )