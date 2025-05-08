import axios from 'axios';
import { useQuery, useMutation } from '@tanstack/react-query';
import queryClient from '../services/queryClient';
import { toast } from 'react-toastify';

export const useUser = (params) => {
  return useQuery({
    queryKey: ['user'],
    queryFn: () => axios.get(`/user/`, { params: params }).then((res) => res.data)});
};

export const useCreateUser = () => {
  return useMutation({
    mutationKey: ['airport'],
    mutationFn: (values) => axios.post(`/register/`, values).then((res) => res.data),
    onMutate: () => {
      queryClient.cancelQueries('user');
    },
    onSettled: (data) => {
      queryClient.invalidateQueries('user');
      if (data) {
        switch (data[0]) {
          case 'success':
            toast.success(data[1]);
            break;
          case 'warning':
            toast.warning(data[1]);
            break;
          case 'error':
            toast.error(data[1]);
            break;
        }
      }
    },
    // onSuccess: (success) => {
    //   console.log('success', success.response);
    //   toast.success(success.re);
    // },
    onError: (err) => {
      toast.error(err.response.data.detail);
      throw err;
    },
  });
};

export const useUpdateUser = () => {
  return useMutation({
    mutationKey: ['airport'],
    mutationFn: (values) => axios.put(`/user/${values.id}`, values).then((res) => res.data),
    onMutate: (values) => {
      queryClient.setQueryData(['user', values.id], values);
    },
    onSuccess: (data, variables) => {
      queryClient.invalidateQueries(['user', variables.id]);
      queryClient.invalidateQueries('user');
      toast.success('Successfully updated user.');
    },
    onError: (err) => {
      toast.error('Error updating user!');
      throw err;
    },
  });
};

export const useDeleteUser = () => {
  return useMutation({
    mutationKey: ['airport'],
    mutationFn: (id) => axios.delete(`/user/${id}`).then((res) => res),
    onSuccess: () => {
      queryClient.invalidateQueries('user');
      toast.success('Successfully deleted user.');
    },
    onError: (err) => {
      toast.error('Error deleting user!');
      throw err;
    },
  });
};
