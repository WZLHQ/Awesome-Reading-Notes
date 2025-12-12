import  torch
import numpy as np

class MultiHeadAttention(torch.nn.Module):

    def __init__(self, in_dim, num_heads, head_dim):

        self.in_dim=in_dim
        self.num_heads=num_heads
        self.head_dim=head_dim

        self.q=torch.nn.Linear(in_dim,num_heads*head_dim)
        self.k=torch.nn.Linear(in_dim,num_heads*head_dim)
        self.v=torch.nn.Linear(in_dim,num_heads*head_dim)
        self.o=torch.nn.Linear(in_dim,num_heads*head_dim)

    def forward(self, x):

        bs, length, _=x.shape()
        
        # forward QKV and reshape
        Q,K,V=self.q(x).reshape(bs, self.num_heads, length, self.head_dim), self.k(x).reshape(bs, self.num_heads, length, self.head_dim), self.v(x).reshape(bs, self.num_heads, length, self.head_dim)

        # compute attention scores
        att_scores=torch.nn.functional.softmax(
            torch.matmul(Q,K.transpose(-2,-1))/np.sqrt(self.head_dim), dim=-1 # TODO self.head_dim£¿
        )

        # compute output
        output=(att_scores@V).reshape(bs,length,-1)
        
        return output

