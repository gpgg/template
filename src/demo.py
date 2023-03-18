import torch

device = 'cuda:0' if torch.cuda.is_available() else 'cpu'
w = torch.ones((3, 1), dtype=torch.float, requires_grad=True, device=device)

print(w)
