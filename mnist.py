import tensorflow as tf

from codecarbon import track_emissions

def reduntant():
    i = 100
    while(i>0):
        i=i-1

@track_emissions()
def train_model():
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0
    model = tf.keras.models.Sequential(
        [
            tf.keras.layers.Flatten(input_shape=(28, 28)),
            tf.keras.layers.Dense(128, activation="relu"),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(10),
        ]
    )
    reduntant()
    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

    model.compile(optimizer="adam", loss=loss_fn, metrics=["accuracy"])

    model.fit(x_train, y_train, epochs=55)

    return model


if __name__ == "__main__":
    lst = ['ayush','yogesh','pavan','syam']
    for i in lst:
        t = len(lst)
    model = train_model()
    for i in range(1000):
        if(i%100==0):
            print(i)
