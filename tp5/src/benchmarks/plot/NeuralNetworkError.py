
import pandas as pd
import plotly.express as px
def neural_network_error_graph(neural_network,epoch,training_set,training_output,test_set,test_output,epsilon=0.001):

    previous_train_weights = None

    errors = []
    data = {}
    for _ in range(1, epoch):
        w_min, i, _, _ = neural_network.train(training_set, training_output, test_expected=test_output,
                                             test_set=test_set, batch_amount=1, max_epoch=1, epsilon=epsilon)

        # test benchmark
        activation_values = neural_network.test_forward_propagation(test_set.copy())
        previous_train_weights = w_min

        test_mse_sum = 0
        for i in range(0, len(activation_values)):
            test_mse_sum += (test_output[i] - activation_values[i]) ** 2

        test_mse = test_mse_sum / len(activation_values)
        errors.append(test_mse[0])
    print(errors)
    test_data = {'Epochs': [i for i in range(1, epoch)], 'test_errors': errors}
    df = pd.DataFrame(test_data)

    fig = px.line(df, x="Epochs", y="test_errors", title="Testing Mean Squared Error", labels={
                  'value': 'Mean Squared Error (MSE)'})
    fig.show()


