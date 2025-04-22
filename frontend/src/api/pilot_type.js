import axios from 'axios';
import { useQuery, useMutation } from '@tanstack/react-query';
import queryClient from '@services/queryClient';
import { toast } from 'react-toastify';

export const usePilotType = (params) => {
  return useQuery({
    queryKey: ['pilotType'],
    queryFn: () => axios.get(`/pilot-type/`, { params: params }).then((res) => res.data)});
};

export const useCreatePilotType = () => {
  return useMutation({
    mutationKey: ['airport'],
    mutationFn: (values) => axios.post(`/pilot-type/`, values).then((res) => res.data),
    onMutate: () => {
      queryClient.cancelQueries('pilotType');
    },
    onSettled: () => {
      queryClient.invalidateQueries('pilotType');
    },
    onSuccess: () => {
      toast.success('Successfully created aircraftCategory.');
    },
    onError: (err) => {
      toast.error('Error creating aircraftCategory!');
      throw err;
    },
  });
};

export const useUpdatePilotType = () => {
  return useMutation({
    mutationKey: ['airport'],
    mutationFn: (values) => axios.put(`/pilot-type/${values.id}`, values).then((res) => res.data),
    onMutate: (values) => {
      queryClient.setQueryData(['pilotType', values.id], values);
    },
    onSuccess: (data, variables) => {
      queryClient.invalidateQueries(['pilotType', variables.id]);
      queryClient.invalidateQueries('pilotType');
      toast.success('Successfully updated aircraftCategory.');
    },
    onError: (err) => {
      toast.error('Error updating aircraftCategory!');
      throw err;
    },
  });
};

export const useDeletePilotType = () => {
  return useMutation({
    mutationKey: ['airport'],
    mutationFn: (id) => axios.delete(`/pilot-type/${id}`).then((res) => res),
    onSuccess: () => {
      queryClient.invalidateQueries('pilotType');
      toast.success('Successfully deleted aircraftCategory.');
    },
    onError: (err) => {
      toast.error('Error deleting aircraftCategory!');
      throw err;
    },
  });
};
