import axios from 'axios';
import { useQuery, useMutation } from '@tanstack/react-query';
import queryClient from '../services/queryClient';
import { toast } from 'react-toastify';

export const useFlight = (params) => {
  return useQuery({
    queryKey: ['flight'],
    queryFn: () => axios.get(`/flight/`, { params: params }).then((res) => res.data)});
};

export const useCreateFlight = () => {
  return useMutation({
    mutationKey: ['flight'],
    mutationFn: (values) => axios.post(`/flight/`, values).then((res) => res.data),
    onMutate: () => {
      queryClient.cancelQueries('flight');
    },
    onSettled: () => {
      queryClient.invalidateQueries('flight');
    },
    onSuccess: () => {
      toast.success('Successfully created flight.');
    },
    onError: (err) => {
      toast.error('Error creating flight!');
      throw err;
    },
  });
};

export const useUpdateFlight = () => {
  return useMutation({
    mutationKey: ['flight'],
    mutationFn: (values) => axios.put(`/flight/${values.id}`, values).then((res) => res.data),
    onMutate: (values) => {
      queryClient.setQueryData(['flight', values.id], values);
    },
    onSuccess: (data, variables) => {
      queryClient.invalidateQueries(['flight', variables.id]);
      queryClient.invalidateQueries('flight');
      toast.success('Successfully updated flight.');
    },
    onError: (err) => {
      toast.error('Error updating flight!');
      throw err;
    },
  });
};

export const useDeleteFlight = () => {
  return useMutation({
    mutationKey: ['flight'],
    mutationFn: (id) => axios.delete(`/flight/${id}`).then((res) => res),
    onSuccess: () => {
      queryClient.invalidateQueries('flight');
      toast.success('Successfully deleted flight.');
    },
    onError: (err) => {
      toast.error('Error deleting flight!');
      throw err;
    },
  });
};
