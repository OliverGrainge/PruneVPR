from typing import Callable
import multiprocessing as mp

from parsers import train_arguments

TRAINING_METHODS = {
    "gsv_cities_dense": "PlaceRec.Training.GSV_Cities.dense_trainer",
    "gsv_cities_structured_sparse": "PlaceRec.Training.GSV_Cities.sparse_structured_trainer"
}

def get_trainer(method: str) -> Callable:
    """
    Dynamically imports and returns the appropriate trainer based on the method.
    
    Args:
        method: The training method to use
        
    Returns:
        The trainer function
        
    Raises:
        ValueError: If the training method is not supported
    """
    if method not in TRAINING_METHODS:
        raise ValueError(f"Unsupported training method: {method}. "
                       f"Available methods: {list(TRAINING_METHODS.keys())}")
    
    module_path = TRAINING_METHODS[method]
    module_name, trainer_name = module_path.rsplit('.', 1)
    
    module = __import__(module_path, fromlist=[trainer_name])
    return getattr(module, trainer_name)

def main():
    args = train_arguments()
    trainer = get_trainer(args.training_method)
    trainer(args)

if __name__ == "__main__":
    mp.set_start_method("fork")
    main()
