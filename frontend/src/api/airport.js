import axios from 'axios';
import {
  useQuery,
  useMutation,
} from '@tanstack/react-query';
import queryClient from '@services/queryClient';
import { toast } from 'react-toastify';

export const useAirport = (params) => {
  return useQuery({
    queryKey:['airport'],
    queryFn: () => axios.get(`/airport/`, { params: params }).then((res) => res.data)});
};

export const useCreateAirport = () => {
  return useMutation({
    mutationKey: ['airport'],
    mutationFn: (values) => axios.post(`/airport/`, values).then((res) => res.data),
    onMutate: () => {
      queryClient.cancelQueries('airport');
    },
    onSettled: () => {
      queryClient.invalidateQueries('airport');
    },
    onSuccess: () => {
      toast.success('Successfully created airport.');
    },
    onError: (err) => {
      toast.error('Error creating airport!');
      throw err;
    },
  });
};

export const useUpdateAirport = () => {
  return useMutation({
    mutationKey: ['airport'],
    mutationFn: (values) => axios.put(`/airport/${values.id}`, values).then((res) => res.data),
    onMutate: (values) => {
      queryClient.setQueryData(['airport', values.id], values);
    },
    onSuccess: (data, variables) => {
      queryClient.invalidateQueries(['airport', variables.id]);
      queryClient.invalidateQueries('airport');
      toast.success('Successfully updated airport.');
    },
    onError: (err) => {
      toast.error('Error updating airport!');
      throw err;
    },
  });
};

export const useDeleteAirport = () => {
  return useMutation({
    mutationKey: ['airport'],
    mutationFn: (id) => axios.delete(`/airport/${id}`).then((res) => res),
    onSuccess: () => {
      queryClient.invalidateQueries('airport');
      toast.success('Successfully deleted airport.');
    },
    onError: (err) => {
      toast.error('Error deleting airport!');
      throw err;
    },
  });
};
